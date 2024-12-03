from flask import Flask, jsonify, render_template
import os
import sys

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Import the original app
from app import app as application

def handler(event, context):
    return application

@application.route('/')
def home():
    return render_template('index.html')

# Vercel requires a specific entry point
def create_app():
    return application
