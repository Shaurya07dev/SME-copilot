import os
import json
from datetime import datetime
import google.generativeai as genai
from src.tools.data_tools import get_business_profile, load_sheet_table, save_decision_log, get_recent_history
from src.tools.analytics_tools import compute_kpis, detect_issues, generate_actions
from src.tools.action_tools import send_email, create_calendar_event, create_task

class OpsPilot:
    def __init__(self, business_id):
        self.business_id = business_id
        self.profile = get_business_profile(business_id=business_id)
        if "error" in self.profile:
            raise ValueError(f"Could not load profile: {self.profile['error']}")
            
        # Initialize LLM
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash')
        else:
            print("Warning: GEMINI_API_KEY not found. LLM features will be disabled.")
            self.model = None

    def run_daily_review(self, date=None):
        """
        Orchestrates the daily review (Planner Agent).
        """
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
            
        print(f"Starting Daily Review for {self.profile['name']} on {date}")
        
        # 1. Analytics Agent Phase
        analytics_result = self.run_analytics(date)
        
        # 2. Advisor Agent Phase
        advisor_result = self.run_advisor(analytics_result, date)
        
        return advisor_result

    def run_analytics(self, date):
        """
        Loads data, computes KPIs, detects issues.
        """
        print("Running Analytics...")
        spreadsheet_id = self.profile.get("spreadsheet_id")
        tables = self.profile.get("tables", {})
        
        # Load Data
        data_snapshot = {}
        for name, range_name in tables.items():
            data_snapshot[name] = load_sheet_table(spreadsheet_id, range_name)
            
        # Compute KPIs
        kpis = compute_kpis(data_snapshot.get("sales", []), self.profile.get("kpis", {}))
        
        # Detect Issues
        issues = detect_issues(kpis, self.profile.get("thresholds", {}))
        
        return {
            "date": date,
            "kpis": kpis,
            "issues": issues,
            "data_snapshot": data_snapshot # Pass specific summaries if needed
        }

    def run_advisor(self, analytics, date):
        """
        Generates actions and briefing.
        """
        print("Running Advisor...")
        issues = analytics["issues"]
        kpis = analytics["kpis"]
        
        # Generate Actions (Rule-based)
        actions = generate_actions(issues)
        
        # Generate Briefing (LLM)
        briefing = self.generate_briefing(kpis, issues, actions)
        
        # Execute Actions (Notifications)
        print("Executing Actions...")
        for action in actions:
            try:
                if action['type'] == 'create_task':
                    create_task(
                        title=action['title'],
                        description=action['description'],
                        spreadsheet_id=self.profile.get("spreadsheet_id")
                    )
                    print(f"Executed: Created Task '{action['title']}'")
                elif action['type'] == 'create_calendar_event':
                    create_calendar_event(
                        summary=action['summary'],
                        description=action['description'],
                        start_time=action['start_time'],
                        end_time=action['end_time']
                    )
                    print(f"Executed: Created Calendar Event '{action['summary']}'")
                elif action['type'] == 'send_email':
                    # We will send a consolidated email below instead of individual ones
                    pass
            except Exception as e:
                print(f"Failed to execute action {action}: {e}")
        
        # Log to DecisionLog
        log_entry = [
            date,
            json.dumps(kpis),
            json.dumps(issues),
            json.dumps([a['type'] for a in actions])
        ]
        save_decision_log(self.profile.get("spreadsheet_id"), log_entry)
        
        # Send Email Report
        if self.model: 
            email_body = briefing
            # Send to the user's requested email
            send_email("shaurya8851@gmail.com", f"Daily Ops Report - {date}", email_body)
            print("Executed: Sent Daily Briefing Email")
            
        return {
            "briefing": briefing,
            "actions": actions
        }

    def generate_briefing(self, kpis, issues, actions):
        if not self.model:
            return f"KPIs: {kpis}\nIssues: {issues}\nActions: {actions}"
            
        prompt = f"""
        You are an Operations Advisor for {self.profile['name']}.
        Date: {datetime.now().strftime('%Y-%m-%d')}
        
        KPIs:
        {json.dumps(kpis, indent=2)}
        
        Issues Detected:
        {json.dumps(issues, indent=2)}
        
        Recommended Actions:
        {json.dumps(actions, indent=2)}
        
        Please write a concise, professional daily briefing for the business owner.
        Summarize performance, highlight critical issues, and explain the recommended actions.
        """
        
        response = self.model.generate_content(prompt)
        return response.text
