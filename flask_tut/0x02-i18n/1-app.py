#!/usr/bin/env python3
"""
Flask app
"""

# Importing required modules from Flask and Flask-Babel libraries
from flask import Flask, render_template
from flask_babel import Babel

# Define a configuration class for Babel settings
class Config(object):
    """
    Configuration for Babel
    """
    # Define the list of languages to support
    LANGUAGES = ["en", "fr"]
    # Default language to use if none is specified
    BABEL_DEFAULT_LOCALE = "en"
    # Default timezone
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Initialize the Flask application
app = Flask(__name__)

# Load configurations from the Config class
app.config.from_object(Config)

# Initialize the Babel extension with the Flask app's configuration
babel = Babel(app)

# Define the index route, mapping it to the root URL ('/')
@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    # Render '1-index.html' template when this route is accessed
    return render_template('1-index.html')

# Start the application, only if this script is executed as the main program
if __name__ == "__main__":
    # Run the app with debugging enabled
    app.run(debug=True)
