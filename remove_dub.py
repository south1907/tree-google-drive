# remove dup files in one folder

import os
import json
import time

start_time = time.time()

with open('folder.txt', 'r') as f:
	folder_id = f.read()

root_path = 'data/' + folder_id
	
all_data = {}
if os.path.isdir(root_path):
	files = os.listdir(root_path)
	for file in files:
		result = []

		with open(root_path + '/' + file, 'r') as f:
			data = json.loads(f.read())['data']

			for item in data:
				if item not in result:
					result.append(item)
				else:
					print('da co file nay trong folder')
					print(item)
			final = {
				"data": result
			}
			f.close()
		with open(root_path + '/' + file, 'w') as f:
			json.dump(final, f, indent=4, ensure_ascii=False)
			f.close()
