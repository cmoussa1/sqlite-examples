from parse_to_db import parse_to_db
import os

path = r"/Users/moussa1/src/sqlite/sqlite-examples"

for filename in os.listdir(path):
	if filename.endswith("santana41.json"):
		print(filename)
		parse_to_db(filename, "Indians")
		fullpath = os.path.join(path, filename)