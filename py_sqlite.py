'''
Python CLI utility/script to parse JSON object and 
store them in an SQLite database.

Author: Christopher Moussa
Date: September 10th, 2019
'''
import json
import sqlite3
import pandas as pd

print("*" * 50)
print("\t\t      PHASE 1")
print("*" * 50)
print("Description: Parse JSON file and read from dictionary")
print()

# open the json file in read mode, store the object as a dictionary
with open('pillar1.json', 'r') as f:
	my_dict = json.load(f)

print("Accessing values by key")
print("-----------------------")
print("playerid: %s" 			% my_dict["playerid"])
print("name: %s" 				% my_dict["name"])
print("jersey_number: %d" 		% my_dict["jersey_number"])
print("primary_position: %s" 	% my_dict["primary_position"])
print("ops: %.3f" 				% my_dict["ops"])
print()

print("Printing dictionary object")
print("--------------------------")
print(json.dumps(my_dict, indent=2))
print()



print("*" * 50)
print("\t\t      PHASE 2")
print("*" * 50)
print("Description: Parse dictionary object and store items in a list")
print()

# initialize empty list, append values to it to be used in a SQLite command
l = []
for val in my_dict:
	l.append(my_dict[val])

print("List of values")
print("--------------")
print(l)
print()



print("*" * 50)
print("\t\t      PHASE 3")
print("*" * 50)
print("Description: Connect to SQLite database and append values")
print()

conn = sqlite3.connect('BaseballPlayers.db')
print("opened BaseballPlayers DB successfully")

# access list elements to be used in SQLite command
conn.execute('''
	INSERT INTO Giants (playerid, name, jersey_number, primary_position, ops)
	VALUES (?, ?, ?, ?, ?);
	''',(l[0], l[1], l[2], l[3], l[4]))
print("insert value into Giants table executed successfully")
l.clear()

print("****************")
print("* Giants Table *")
print("****************")
print(pd.read_sql_query("SELECT * FROM Giants", conn))
print()
print("print query successful")



print("*" * 50)
print("\t\t      PHASE 4")
print("*" * 50)
print("Description: Read multiple JSON objects into a Python dictionary")
print()

# data will be a list of dictionaries 
with open('players.json') as json_file:
	data = json.load(json_file)

print("JSON file loaded successfully")
print()

print("Printing val from one of the dictionary objects")
print("-----------------------------------------------")
print(data[0]["name"]) # accessing dictionary value with the following syntax
print()



print("*" * 50)
print("\t\t      PHASE 5")
print("*" * 50)
print("Description: Adding multiple dictionary objects to a SQLite table")
print()

print("Printing multiple dictionary objects from JSON file")
print("Adding multiple dictionary objects to a SQLite table")
print("---------------------------------------------------")
for d in data: # for each dictionary in the list of dictionaries
	for k, v in d.items():
		print("%s: %s" % (k, v))
		l.append(v) # same process as before
	conn.execute('''
		INSERT INTO Giants (playerid, name, jersey_number, primary_position, ops)
		VALUES (?, ?, ?, ?, ?);
		''',(l[0], l[1], l[2], l[3], l[4]))
	print("insert value into Giants table executed successfully")
	l.clear()
	print()

print("****************")
print("* Giants Table *")
print("****************")
print(pd.read_sql_query("SELECT * FROM Giants", conn))
print()
print("print query successful")















