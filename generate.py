import os
import json

with open('folder.txt', 'r') as f:
	folder_id = f.read()

root_path = 'data/' + folder_id
	
all_data = {}
if os.path.isdir(root_path):
	files = os.listdir(root_path)
	for file in files:
		with open(root_path + '/' + file, 'r') as f:
			data = json.loads(f.read())['data']

			all_data[file.split('.')[0]] = data

def generateFolder(data, folder_id):
	result = []

	if folder_id in data:
		items = data[folder_id]

		for item in items:
			if item['mimeType'] == 'application/vnd.google-apps.folder':
				item['children'] = generateFolder(data, item['id'])

			result.append(item)

	return result

final = generateFolder(all_data, folder_id)
with open('output/' + folder_id +'.json', 'w') as outfile:
	json.dump(final, outfile, indent=4, ensure_ascii=False)
