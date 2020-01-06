### Some query example

results = service.files().list(q="'root' in parents and name contains 'training' and mimeType='application/vnd.google-apps.folder'").execute()

results = service.files().list(pageSize=2, driveId='1VvMyjU_VeOqPueEsj9Rcrk1ll434rUAx', q="mimeType='application/vnd.google-apps.folder'", includeItemsFromAllDrives=True, corpora="drive", supportsAllDrives=True, fields='nextPageToken, files(id, name, mimeType)', pageToken=page_token).execute()

### Setup

1. copy file folder.txt from file folder.example.txt --> edit id of folder need run
2. run file main.py