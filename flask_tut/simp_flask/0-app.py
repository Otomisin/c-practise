#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)