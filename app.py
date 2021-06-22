from flask import Flask, render_template, request

import os
import sqlite3 as sql
import pandas as pd
#import numpy as np
#import random
#import datetime
import json
import plotly

DATABASE = os.path.abspath(os.path.dirname(__file__)) + "/test_db.db"
RAW_DATA_TABLE = 'test_data_table'

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/test")
def login_page():
    return render_template("test.html")

@app.route("/_test_query", methods=['GET', 'POST'])
def get_test_row():
    test_rows = []
    with sql.connect(DATABASE) as connection:
        try:
            cur = connection.cursor() # create a cursor to write SQL commands to database
            cur.execute("SELECT * FROM {}".format(RAW_DATA_TABLE))  # execute command on the relevant table (* means all)
            rows = cur.fetchall() # grab all the resulting rows from the above query
            df = pd.DataFrame(rows) # store the rows into a pandas dataframe
            df.columns = [tuple[0] for tuple in cur.description] # grab the headers from the sql columns and assign the pandas df headers accordingly
            for index, row in df.iterrows(): # add each row in the dataframe to the list that gets sent back to the client
                test_rows.append(row['test_string'] + ", " + str(row['test_int']))
        except Exception as e:
            connection.rollback()
            print("error querying room numbers from database...Exception: " + str(e))
    update_dict = dict(test_results = test_rows, response_string = "communication OK") # create a dict of variables to send back to client
    update = json.dumps(update_dict, cls=plotly.utils.PlotlyJSONEncoder) # here's an example of a plotly encoder as well as a json dump
    return update # send response back to client in JSON format


if __name__ == "__main__":
    print('[INFO] Starting server at http://localhost:5000')
    app.run(host="0.0.0.0", port="5000", debug=True)
    
