import json
import os

def get_business_profile(profile_path="data/profiles.json", business_id=None):
    """
    Reads the business profile configuration.
    """
    if not os.path.exists(profile_path):
        return {"error": f"Profile file not found at {profile_path}"}
    
    try:
        with open(profile_path, 'r') as f:
            profiles = json.load(f)
            
        if business_id:
            return profiles.get(business_id, {"error": "Business ID not found"})
        return profiles
    except Exception as e:
        return {"error": str(e)}

from googleapiclient.discovery import build
from src.utils.auth import get_credentials
import pandas as pd
from datetime import datetime

def load_sheet_table(spreadsheet_id, range_name, service_account_file=None):
    """
    Loads data from a Google Sheet into a list of dictionaries (records).
    """
    creds = get_credentials(service_account_file)
    if not creds:
        return {"error": "Authentication failed"}

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=range_name).execute()
        values = result.get('values', [])

        if not values:
            return []

        # Assume first row is header
        headers = values[0]
        data = []
        for row in values[1:]:
            # Pad row with empty strings if it's shorter than headers
            row += [''] * (len(headers) - len(row))
            record = dict(zip(headers, row))
            data.append(record)
            
        return data
    except Exception as e:
        return {"error": str(e)}

def save_decision_log(spreadsheet_id, log_entry, worksheet_name="DecisionLog", service_account_file=None):
    """
    Appends a decision log entry to the specified worksheet.
    log_entry should be a list of values matching the sheet columns.
    Example: [Date, KPI_Summary, Issues, Actions]
    """
    creds = get_credentials(service_account_file)
    if not creds:
        return {"error": "Authentication failed"}

    try:
        service = build('sheets', 'v4', credentials=creds)
        
        # Prepare the values to append
        # If log_entry is a dict, convert to list based on expected schema? 
        # For now, assume list for simplicity or handle simple dict conversion if needed.
        # Let's assume log_entry is a list of strings.
        
        body = {
            'values': [log_entry]
        }
        
        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=f"{worksheet_name}!A1",
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()
        
        return {"status": "success", "updatedRange": result.get('updates', {}).get('updatedRange')}
    except Exception as e:
        return {"error": str(e)}

def get_recent_history(spreadsheet_id, n_days=7, worksheet_name="DecisionLog", service_account_file=None):
    """
    Reads the last N rows from the DecisionLog.
    """
    # Reuse load_sheet_table logic but we might need to handle 'last N' specifically.
    # For simplicity, load all and slice.
    data = load_sheet_table(spreadsheet_id, worksheet_name, service_account_file)
    if isinstance(data, dict) and "error" in data:
        return data
        
    return data[-n_days:] if data else []

