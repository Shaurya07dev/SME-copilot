import argparse
import os
from dotenv import load_dotenv
from src.agents.ops_pilot import OpsPilot

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description="OpsPilot - AI Operations Co-Pilot")
    parser.add_argument("--business", type=str, default="cafe_delight", help="Business ID to run for")
    parser.add_argument("--date", type=str, help="Date to run review for (YYYY-MM-DD)")
    
    args = parser.parse_args()
    
    try:
        pilot = OpsPilot(args.business)
        result = pilot.run_daily_review(args.date)
        
        print("\n=== Daily Briefing ===")
        print(result["briefing"])
        print("\n=== Actions Generated ===")
        for action in result["actions"]:
            print(f"- [{action.get('type')}] {action.get('title') or action.get('subject')}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
