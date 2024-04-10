from flask import Flask, render_template as RT  # type: ignore

app = Flask(__name__, template_folder="static", static_folder="static")

@app.route("/")
def hello_world():
    return RT("index.html", data=[1, 2, 3, 4, 5])
