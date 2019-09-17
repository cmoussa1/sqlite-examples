import sqlite3
import pandas as pd

# opens a connection to the SQLite database file. If the 
# database is opened successfully, a connection object is
# returned.
conn = sqlite3.connect('BaseballPlayers.db')
print("opened BaseballPlayers DB successfully")
print("-" * 25)

print("****************")
print("* Giants Table *")
print("****************")
print(pd.read_sql_query("SELECT * FROM Giants", conn))
print()
print("print query successful")
print("-" * 25)

# this will execute an SQL statement, which can be parameterized
# (placeholders instead of SQL literals)
#
# Example
# conn.execute("INSERT INTO people VALUES (?, ?)", (who, age))
# 
# we can also use conn.executescript to execute multiple SQL 
# statements at once provided in the form of a script
# 
# the following command is for adding an instance to an existing table
conn.execute('''
	INSERT INTO Giants (playerid, name, jersey_number, primary_position, ops)
	VALUES ('belt9', 'Brandon Belt', 9, '1B', .733 );
	''')
print("insert value into Giants table executed successfully")
print("-" * 25)

# to print the table in nice format, we use pandas
# to output the table
print("****************")
print("* Giants Table *")
print("****************")
print(pd.read_sql_query("SELECT * FROM Giants", conn))
print()
print("print query successful")
print("-" * 25)

conn.execute('''
	CREATE TABLE Dodgers (
		playerid 			TEXT 	PRIMARY KEY NOT NULL,
		name 				TEXT 	NOT NULL,
		jersey_number		INT 	NOT NULL,
		primary_position	TEXT	NOT NULL,
		ops 				REAL	NOT NULL);
	''')
print("Dodgers table created successfully")
print("-" * 25)

conn.execute('''
	INSERT INTO Dodgers (playerid, name, jersey_number, primary_position, ops)
	VALUES ('turner10', 'Justin Turner', 10, '3B', .888 );
	''')
print("insert into Dodgers table executed successfully")
print("-" * 25)

print("*****************")
print("* Dodgers Table *")
print("*****************")
print(pd.read_sql_query("SELECT * FROM Dodgers", conn))
print()
print("print query successful")
print("-" * 25)

conn.close()