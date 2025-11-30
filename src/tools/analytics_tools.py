import pandas as pd
from datetime import datetime

def compute_kpis(data, kpi_config):
    """
    Computes KPIs based on data and configuration.
    data: list of dicts (records)
    kpi_config: dict defining KPIs (e.g., {"revenue": {"column": "Amount", "op": "sum"}})
    """
    if not data:
        return {}
    
    df = pd.DataFrame(data)
    results = {}
    
    for kpi_name, config in kpi_config.items():
        col = config.get("column")
        op = config.get("op")
        
        if col not in df.columns:
            results[kpi_name] = 0 # Or error
            continue
            
        # Ensure numeric
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass # Handle non-numeric gracefully?
            
        if op == "sum":
            results[kpi_name] = float(df[col].sum())
        elif op == "count":
            results[kpi_name] = int(df[col].count())
        elif op == "mean":
            results[kpi_name] = float(df[col].mean())
            
    return results

def detect_issues(kpis, thresholds):
    """
    Compares KPIs against thresholds to detect issues.
    """
    issues = []
    
    for kpi, value in kpis.items():
        # Check min thresholds
        if f"min_{kpi}" in thresholds:
            limit = thresholds[f"min_{kpi}"]
            if value < limit:
                issues.append(f"Low {kpi}: {value} (Target: >{limit})")
                
        # Check max thresholds
        if f"max_{kpi}" in thresholds:
            limit = thresholds[f"max_{kpi}"]
            if value > limit:
                issues.append(f"High {kpi}: {value} (Target: <{limit})")
                
    return issues

def generate_actions(issues, playbooks=None):
    """
    Maps issues to actions based on playbooks (rules).
    For now, we'll use a simple default mapping if no playbook provided.
    """
    actions = []
    
    # Default simple rules
    for issue in issues:
        if "Low revenue" in issue:
            actions.append({
                "type": "create_task",
                "title": "Investigate low revenue",
                "description": f"Revenue is below target. {issue}"
            })
            actions.append({
                "type": "send_email",
                "subject": "Alert: Low Revenue",
                "body": f"Attention required. {issue}"
            })
            })
        elif "Low inventory" in issue:
             actions.append({
                "type": "create_task",
                "title": "Restock Inventory",
                "description": f"Inventory levels critical. {issue}"
            })
        elif "Low staff_count" in issue:
            actions.append({
                "type": "create_calendar_event",
                "summary": "Emergency Staff Meeting",
                "description": f"Staff count is critically low. {issue}",
                "start_time": datetime.now().isoformat(),
                "end_time": datetime.now().isoformat() # In real app, would add 1 hour
            })
            
    return actions
