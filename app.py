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
            cur = connection.cursor()
            cur.execute("SELECT * FROM {}".format(RAW_DATA_TABLE))
            rows = cur.fetchall()
            df = pd.DataFrame(rows)
            df.columns = [tuple[0] for tuple in cur.description]
            for index, row in df.iterrows():
                test_rows.append(row['test_string'] + ", " + str(row['test_int']))
        except Exception as e:
            connection.rollback()
            print("error querying room numbers from database...Exception: " + str(e))
    update_dict = dict(test_results = test_rows, response_string = "communication OK")
    update = json.dumps(update_dict, cls=plotly.utils.PlotlyJSONEncoder)
    print(test_rows)
    return update


if __name__ == "__main__":
    print('[INFO] Starting server at http://localhost:5000')
    app.run(host="0.0.0.0", port="5000", debug=True)
    
