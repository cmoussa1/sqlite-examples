import json
import sqlite3
import pandas as pd

def parse_to_db(f, table):
	conn = sqlite3.connect('BaseballPlayers.db')
	print("opened BaseballPlayers DB successfully")

	with open(f) as json_file:
		data = json.load(json_file)	

	print("JSON file loaded successfully...")

	l = []

	# Val
	if (type(data) == dict):
		for key, val in data.items():
			# print(type(val))
			print("%s: %s" % (key, val))
			# is the object a nested list?
			if (type(val) == list):
				for nested_val in val:
					for item in nested_val:
						l.append(nested_val[item])
			# is the object a nested dictionary?
			elif (type(val) == dict):
				for nested_val in val:
					l.append(val[nested_val])
			# anything else
			else:
				l.append(val)
		print(l)
		conn.execute('''
			INSERT INTO Giants
			VALUES (?, ?, ?, ?, ?);
			''',(l[0], l[1], l[2], l[3], l[4]))
		print("insertion into " + table + " table executed successfully...")
		l.clear()
		print()
	else:
		for d in data:
			for key, val in d.items():
				# print(type(val))
				print("%s: %s" % (key, val))
				# is the object a nested list?
				if (type(val) == list):
					for nested_val in val:
						for item in nested_val:
							l.append(nested_val[item])
				# is the object a nested dictionary?
				elif (type(val) == dict):
					for nested_val in val:
						l.append(val[nested_val])
				# anything else
				else:
					l.append(val)
			print(l)
			conn.execute('''
				INSERT INTO Giants
				VALUES (?, ?, ?, ?, ?);
				''',(l[0], l[1], l[2], l[3], l[4]))
			print("insertion into " + table + " table executed successfully...")
			l.clear()
			print()

	print("****************")
	print("* " + table + " Table *")
	print("****************")
	sql = "SELECT * FROM " + table
	print(pd.read_sql_query(sql, conn))
	print()
	print("print query successful...")

	# make the changes persistent in our database
	# conn.commit()

parse_to_db("vogt21.json", "Giants")