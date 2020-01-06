### Some query example

results = service.files().list(q="'root' in parents and name contains 'training' and mimeType='application/vnd.google-apps.folder'").execute()

results = service.files().list(pageSize=2, driveId='1VvMyjU_VeOqPueEsj9Rcrk1ll434rUAx', q="mimeType='application/vnd.google-apps.folder'", includeItemsFromAllDrives=True, corpora="drive", supportsAllDrives=True, fields='nextPageToken, files(id, name, mimeType)', pageToken=page_token).execute()

### Setup

1. go https://console.developers.google.com/apis/credentials, create and download file credentials.json
or go https://developers.google.com/drive/api/v3/quickstart/python, enable the Drive API, download file credentials.json
2. copy file folder.txt from file folder.example.txt --> edit id of folder need run
3. run file main.py