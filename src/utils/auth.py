import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/gmail.send'
]

def get_credentials(service_account_file=None):
    """
    Gets credentials for Google APIs.
    Prioritizes Service Account if provided, otherwise tries OAuth User credentials.
    """
    creds = None
    
    # 1. Try Service Account
    # Calculate project root relative to this file (src/utils/auth.py -> root)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    default_service_account = os.path.join(base_dir, 'service_account.json')
    
    if not service_account_file and os.path.exists(default_service_account):
        service_account_file = default_service_account

    if service_account_file and os.path.exists(service_account_file):
        print(f"Using Service Account: {service_account_file}")
        creds = Credentials.from_service_account_file(
            service_account_file, scopes=SCOPES)
        return creds

    # 2. Try OAuth User Credentials (token.pickle)
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if os.path.exists('credentials.json'):
                 # Client Secret file for OAuth
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            else:
                 print("No credentials.json or service_account.json found.")
                 return None
                 
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds
