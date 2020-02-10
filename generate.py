import os
import json
import time

start_time = time.time()

with open('folder.txt', 'r') as f:
	folder_id = f.read().strip()

root_path = 'data/' + folder_id
	
all_data = {}
if os.path.isdir(root_path):
	files = os.listdir(root_path)
	for file in files:
		with open(root_path + '/' + file, 'r') as f:
			data = json.loads(f.read())['data']

			all_data[file.split('.')[0]] = data

checked = []

def generateFolder(data, folder_id):
	result = []

	checked.append(folder_id)
	print(len(checked))
	if folder_id in data:
		items = data[folder_id]

		for item in items:
			if item['mimeType'] == 'application/vnd.google-apps.folder':
				if item['id'] not in checked:
					item['children'] = generateFolder(data, item['id'])
				else:
					print('da duyet roi, co the bi lap')
					print(folder_id)

			result.append(item)

	return result

final = generateFolder(all_data, folder_id)

end_time = time.time()
print('total time: ')
print(end_time - start_time);

with open('output/' + folder_id +'.json', 'w') as outfile:
	json.dump(final, outfile, indent=4, ensure_ascii=False)
