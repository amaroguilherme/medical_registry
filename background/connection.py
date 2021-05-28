from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from settings import SCOPES

def get_connection():
    creds = None

    if os.path.exists('resources/token.json'):
        creds = Credentials.from_authorized_user_file('resources/token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'resources/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('resources/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    return sheet