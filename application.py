from logging import debug
import re
from flask import Flask, render_template, request
import client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/startDemo", methods = ["GET", "POST"])
def startDemo():
    if(request.method == "POST"):
        print(request.form["port"], request.form["message"])
    return client.main(request.form["port"], request.form["message"])

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug = True)