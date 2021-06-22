from flask import Flask, render_template, request

#import pandas as pd
#import numpy as np
#import random
#import datetime


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/test")
def login_page():
    return render_template("test.html")





if __name__ == "__main__":
    print('[INFO] Starting server at http://localhost:5000')
    app.run(host="0.0.0.0", port="5000", debug=True)
    
