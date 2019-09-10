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
	for d in data:
		for key, val in d.items():
			print("%s: %s" % (key, val))
			l.append(val)
		conn.execute('''
			INSERT INTO Giants (playerid, name, jersey_number, primary_position, ops)
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
	conn.commit()