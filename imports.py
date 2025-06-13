from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth
import os
from googleapiclient.http import MediaFileUpload
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = Credentials.from_authorized_user_file("token.json", SCOPES)
LOC_PATH = "/home/ampar/Sync_Folder"
ID_PATH = "/home/ampar/Workspace/AutoSync/folder_id.txt"
DIR_DETAILS= "/home/ampar/Workspace/AutoSync/Zipop/addresses.txt"
service = build("drive" , "v3" , credentials= creds)

def folder_exists(FILE_ID):
    try:
        folder = service.files().get(fileId = FILE_ID , fields = 'id , mimeType').execute()
        if folder['mimeType'] == "application/vnd.google-apps.folder":
            return True
        else:
            print("ID exists but no folder.Resolve!")
            return False
    except HttpError as error:
        if error.resp.status == 404 :
            print("Folder Not Found")
            return False
        else:
            print(error)
            return False