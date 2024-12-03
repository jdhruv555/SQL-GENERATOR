from flask import Flask, render_template, jsonify, request
import os
import sys

# Ensure the project root is in the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Import necessary modules
from dotenv import load_dotenv
load_dotenv()

# Create Flask app
app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

# Import routes from main application
from app import *

# Vercel serverless function entry point
def handler(event, context):
    return app

# Fallback route
@app.route('/')
def home():
    return render_template('index.html')

# Additional error handling
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify(error=str(e)), 500

# Ensure the app can be imported and used
application = app
