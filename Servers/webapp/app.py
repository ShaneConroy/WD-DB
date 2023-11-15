from flask import Flask, render_template, request

app = Flask(__name__)


""" 
HTTP Status Codes:
    100-199: Informational.
    200-299: OK.
    300-399: Redirects.
    400-499: Client-errors.
    500-599: Server-errors.
"""


@app.get("/showform")
def display_the_form():
    return render_template(
        "form.html",        
        title="Form page",
        heading="Give me your details",
        footer="Form footer text",
    )


@app.post("/processform")
def save_data_to_file():
    the_id = request.form["the_id"]
    the_name = request.form["the_name"]
    the_password = request.form["the_password"]

    print(the_id, the_name, the_password)
    
    return render_template(
        "results.html",
        title="Results page",
        heading="Here is your results",
        footer="Results footer text",    
        id=request.form["the_id"],
        name=the_name,
        password=the_password,  
    )


@app.get("/")  # The default web location of this webapp.
def homepage():
    return "Hello from my first Flask-based webapp."


@app.get("/other")  # The /other bit is a URL.
def otherpage():
    1 / 0
    return "This is the FIXED other page - no more 1 / 0."


@app.get("/chart")
def display_chart():
    return render_template(
        "bar.html",
        title="Chart page",
        heading="Here is your chart",
        footer="Chart footer text",
    )


if __name__ == "__main__":
    app.run(debug=True)
