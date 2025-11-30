from googleapiclient.discovery import build
from src.utils.auth import get_credentials
import base64
from email.mime.text import MIMEText

def send_email(to, subject, body, service_account_file=None):
    """
    Sends an email using the Gmail API.
    Note: Service Accounts need Domain-Wide Delegation to impersonate a user to send email.
    If using standard OAuth (token.pickle), it works directly.
    """
    creds = get_credentials(service_account_file)
    if not creds:
        return {"error": "Authentication failed"}

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        body = {'raw': raw}
        
        message = service.users().messages().send(userId='me', body=body).execute()
        return {"status": "sent", "id": message['id']}
    except Exception as e:
        return {"error": str(e)}

def create_calendar_event(summary, start_time, end_time, description="", service_account_file=None):
    """
    Creates a Google Calendar event.
    Times should be ISO format strings.
    """
    creds = get_credentials(service_account_file)
    if not creds:
        return {"error": "Authentication failed"}

    try:
        service = build('calendar', 'v3', credentials=creds)
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_time,
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'UTC',
            },
        }
        
        event = service.events().insert(calendarId='primary', body=event).execute()
        return {"status": "created", "link": event.get('htmlLink')}
    except Exception as e:
        return {"error": str(e)}

def create_task(title, description, spreadsheet_id=None, worksheet_name="Tasks", service_account_file=None):
    """
    Creates a task. 
    If spreadsheet_id is provided, appends to a 'Tasks' sheet.
    Otherwise, just logs it (or could call Trello/Jira).
    """
    if spreadsheet_id:
        creds = get_credentials(service_account_file)
        if not creds:
            return {"error": "Authentication failed"}
            
        try:
            service = build('sheets', 'v4', credentials=creds)
            values = [[title, description, "Pending", datetime.now().isoformat()]]
            body = {'values': values}
            
            service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id,
                range=f"{worksheet_name}!A1",
                valueInputOption="USER_ENTERED",
                body=body
            ).execute()
            return {"status": "created_in_sheet"}
        except Exception as e:
            return {"error": str(e)}
            
    return {"status": "simulated", "info": f"Task '{title}' created (no backend configured)"}

from datetime import datetime
