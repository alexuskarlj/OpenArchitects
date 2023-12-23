# Import necessary modules and libraries
from flask import Flask, render_template
from .config import Config  # Import configuration settings
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database
from flask_cors import CORS  # Import CORS for handling cross-origin requests

# Create a Flask web application instance
app = Flask(__name__, static_url_path='/app/static', static_folder='static')

# Load configuration settings for the Flask app
app.config.from_object(Config)

# Initialize a SQLAlchemy database connection
db = SQLAlchemy(app)

# Initialize CORS (Cross-Origin Resource Sharing) to handle cross-origin requests
CORS(app)

# Import routes defined in the 'app.routes' module
from app.routes import bp

# Register the blueprint (routing rules) for the Flask app
app.register_blueprint(bp)

# Define a route for the root URL ('/') and render the 'index.html' template
@app.route('/')
def index():
    return render_template('index.html')

# Import database models defined in the 'app.models' module
from app import models
