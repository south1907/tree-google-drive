from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import os
import sys, traceback

root_os = os.path.dirname(os.path.abspath(__file__)) + '/'
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
limit_request = 500
def getFolder(service, folder_id="root"):
	
	print(folder_id)
	results = []
	page_token = None
	limit_page = 20
	count = 0
	while count < limit_page:
		# Call the Drive v3 API
		count += 1
		try:
			response = service.files().list(q="'"+ folder_id +"' in parents").execute()

			page_token = response.get('nextPageToken', None)
			items = response.get('files', [])

			if not items:
				break
			else:
				for item in items:
					if item not in results:
						results.append(item)

			if page_token is None:
				break

			print('next page')
		except Exception as e:
			traceback.print_exc(file=sys.stdout)
			print('loi roi')
		

	return results

def main():

	creds = None

	if os.path.exists(root_os + 'token.pickle'):
		with open(root_os + 'token.pickle', 'rb') as token:
			creds = pickle.load(token)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(root_os + 
				'credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open(root_os + 'token.pickle', 'wb') as token:
			pickle.dump(creds, token)

	service = build('drive', 'v3', credentials=creds)

	with open(root_os + 'folder.txt', 'r') as f:
		root = f.read().strip()

	root_path = root_os + 'data/' + root
	
	all_data = {}
	if os.path.isdir(root_path):
		files = os.listdir(root_path)
		for file in files:
			with open(root_path + '/' + file, 'r', encoding="utf-8") as f:
				data = json.loads(f.read())['data']

				all_data[file.split('.')[0]] = data


	queue_folder = []

	if bool(all_data):
		for (key,value) in all_data.items():
			for it in value:
				if it['id'] not in all_data and it['mimeType'] == 'application/vnd.google-apps.folder':
					queue_folder.append(it['id'])
	else:
		print('empty')
		queue_folder = [root]

	count = 0
	while len(queue_folder) > 0 and count < limit_request:
		new_queue_folder = []
		for folder_id in queue_folder:
			count += 1
			print(count)
			items = getFolder(service, folder_id)
			for item in items:
				if item['mimeType'] == 'application/vnd.google-apps.folder':
					new_queue_folder.append(item['id'])
			data_file = {
				'data': items
			}

			if not os.path.isdir(root_path):
				os.mkdir(root_path)
			with open(root_path + '/' + folder_id +'.json', 'w', encoding="utf-8") as outfile:
				json.dump(data_file, outfile, indent=4, ensure_ascii=False)

			if count > limit_request:
				break

		# print(new_queue_folder)
		queue_folder = new_queue_folder
	
	print("Count: " + str(count))

if __name__ == '__main__':
	main()
