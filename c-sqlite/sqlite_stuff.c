/*
  sqlite3_open(const char *filename, sqlite3 **ppDb)

  This routine opens a connection to an SQLite database file and
  returns a database connection object to be used by other SQLite
  routines.

  If the filename argument is NULL or ':memory:', sqlite3_open()
  will create an in-memory database in RAM that lasts only for
  the duration of the session.

  If the filename is not NULL, sqlite3_open() attempts to open the
  database file by using its value. If no file by that name exists,
  sqlite3_open() will open a new database file by that name.

  ----------

  sqlite3_exec(sqlite3*, const char *sql, sqlite_callback, void *data,
    char **errmsg)

  This routine provides a quick, easy way to execute SQL commands
  provided by sql argument which can consist of more than one SQL
  command.

  Here, the first argument sqlite3 is an open database object,
  sqlite_callback is a call back for which data is the 1st argument
  and errmsg will be returned to capture any error raised by the routine.

  SQLite3_exec() routine parses and executes every command given in
  the sql argument until it reaches the end of the string or encounters
  an error.

  ----------

  sqlite3_close(sqlite3*)

  This routine closes a database connection previously opened by a call
  to sqlite3_open(). All prepared statements associated with the connection
  should be finalized prior to closing the connection.

  If any queries remain that have not been finalized, sqlite3_close() will
  return SQLITE_BUSY with the error message "Unable to close due to unfinalized
  statements"
*/

#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>

/*
This callback function provides us a way to obtain results from
SELECT statements. It has the following declaration -

  - void*:  Data provided in the 4th argument of sqlite3_exec()
  - int:    The number of columns in a row
  - char**: An array of strings representing fields in the row
  - char**: An array of strings representing column names

If this callback is provided in the sqlite_exec() routine as
the third argument, SQLite will call this callback function for
each record processed in each SELECT statement executed within the
SQL argument.
*/
static int callback(void *NotUsed, int argc, char** argv, char** azColName) {
  int i;
  for (i = 0; i < argc; i++) {
    printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
  }
  printf("\n");
  return 0;
}

int main(int argc, char* argv[]) {
  sqlite3 *db;
  char *zErrMsg = 0;
  int rc;
  char* sql;
  const char* data = "Callback function called";

  // Open Database
  rc = sqlite3_open("PeopleOfAZ.db", &db);

  if (rc) {
    fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
    return(0);
  }
  else {
    fprintf(stderr, "Opened database successfully\n");
  }

  /* Create table in database

  // Create SQL CREATE statement
  sql = "CREATE TABLE COMPANY(" \
    "ID       INT PRIMARY KEY   NOT NULL," \
    "NAME     TEXT              NOT NULL," \
    "AGE      TEXT              NOT NULL," \
    "ADDRESS  CHAR(50)," \
    "SALARY   REAL);";

  */

  /*
  // Create SQL INSERT statement
  sql = "INSERT INTO COMPANY VALUES " \
    "(1, 'Paul', 32, 'California', 20000.00);" \
        "INSERT INTO COMPANY VALUES " \
    "(2, 'Allen', 25, 'Texas', 15000.00);";
  */

  /*
  // Create SQL SELECT statement
  sql = "SELECT * FROM COMPANY";
  */

  // Create SQL UPDATE statement
  sql = "UPDATE COMPANY SET SALARY = 25000.00 WHERE ID=1; " \
    "SELECT * FROM COMPANY;";

  // Execute SQL statement
  rc = sqlite3_exec(db, sql, callback, (void*)data, &zErrMsg);

  if (rc != SQLITE_OK) {
    fprintf(stderr, "SQL Error: %s\n", zErrMsg);
    sqlite3_free(zErrMsg);
  }
  else {
    fprintf(stdout, "Operation done successfully\n");
  }

  sqlite3_close(db);
  return 0;
}
