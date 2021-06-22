import os
import sqlite3 as sql
import numpy as np
import pandas as pd
# need xlrd to read old style .xls excel files [pip install xlrd]
# need odfpy to read .ods files [pip install odfpy]

DATABASE = os.path.abspath(os.path.dirname(__file__)) + "/test_db.db"
RAW_DATA_TABLE = 'test_data_table'

# In the following code, deliberately keep each section seperate for demonstration purposes.

# delete the table if it already exists, we will create it again from the origin csv data files
with sql.connect(DATABASE) as connection:
    try:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS {}".format(RAW_DATA_TABLE))
        connection.commit()
        print("Deleted table: '{}' from database: '{}'".format(RAW_DATA_TABLE, DATABASE))
    except Exception as e:
        connection.rollback()
        print("error creating database/table...Exception: " + str(e))


# Create the database and a table for data
with sql.connect(DATABASE) as connection:
    try:
        cursor = connection.cursor()
        query_string = "CREATE TABLE IF NOT EXISTS {} (test_string TEXT, test_int INT)".format(RAW_DATA_TABLE)
        cursor.execute(query_string)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("error creating database/table...")
        print("Exception: " + str(e))


with sql.connect(DATABASE) as con:
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO {} (test_string, test_int) VALUES (?,?)".format(RAW_DATA_TABLE),("test", 1))
        print("Populated table: '{}' in database: '{}' with some test data".format(RAW_DATA_TABLE, DATABASE))
    except Exception as e:
        con.rollback()
        print("Error writing to database. Exception: " + str(e))