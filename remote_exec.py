from parse_to_db import parse_to_db
import os

path = r"/Users/moussa1/src/sqlite/sqlite-examples"

for filename in os.listdir(path):
	if filename.endswith(".json"):
		print(filename)
		parse_to_db(filename, "Giants")
		fullpath = os.path.join(path, filename)