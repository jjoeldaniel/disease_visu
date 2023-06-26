from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    """Our default routes of '/' and '/index'

    Return: The content we want to display to a user
    """

    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/map")
def map():
    return render_template("map.html")


@app.route("/<path:path>")
def catch_all(path):
    """A special route that catches all other requests

    Note: Let this be your last route. Priority is defined
    by order, so placing this above other functions will
    cause catch_all() to override then.

    Return: A redirect to our index route
    """

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
