#!/usr/bin/python3

"""
Defines a basic flask web app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text='is cool'):
    return "Python " + text.replace("_", " ")


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_tempalte_route(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    if isinstance(n, int):
        if n % 2:
            eo = "odd"
        else:
            eo = "even"
        return render_template("6-number_odd_or_even.html", n=n, eo=eo)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
