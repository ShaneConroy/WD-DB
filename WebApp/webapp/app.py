from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")  # The default web location of this webapp.
def homepage():
    return "Hello from my first Flask-based webapp."


@app.get("/other")  # The /other bit is a URL.
def otherpage():
    return "This is the other page."

@app.get("/chart")
def display_chart():
    return render_template("bar.html")

if __name__ == "__main__":
    app.run(debug=True)