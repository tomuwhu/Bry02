from flask import Flask, render_template as RT  # type: ignore

app = Flask(__name__, template_folder="static", static_folder="static")

@app.route("/")
def root():
    return RT("index.html", data=[1, 2, 3, 4, 5])

@app.route("/data")
def getdata():
    return [4, 5, 6, 7, 8, 1, 2]