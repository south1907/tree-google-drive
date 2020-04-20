import json
import os
import time

start_time = time.time()

def create_folder(path):
	try:
		os.makedirs(path)
	except:
		print('path exists')

def create_file(path, file):
	# try:
	with open(os.path.join(path, file), 'w') as fp: 
		pass
	# except:
	# 	print('create file error')

def create_structure(root, drive):
	name = drive['name']
	if drive['mimeType'] == 'application/vnd.google-apps.folder':
		current_path = root + '/' + name.replace('/', '-')
		create_folder(current_path)

		# if have children (because duplicate folder, some folder not get children)
		if 'children' in drive:
			for sub in drive['children']:
				create_structure(current_path, sub)

	else:
		create_file(root, name.replace('/', '-'))

with open('folder.txt', 'r') as f:
	folder_id = f.read().strip()

with open('output/' + folder_id + '.json') as f:
	data = json.loads(f.read())

create_in_folder = 'structure'

for drive_root in data:
	create_structure(create_in_folder + '/' + folder_id, drive_root)

end_time = time.time()
total_time = end_time - start_time
print('total_time: ' + str(total_time))