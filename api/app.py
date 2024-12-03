from flask import Flask, render_template, jsonify, request
import os
import sys

# Ensure the project root is in the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

# Import your original routes and functionality
from app import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Vercel!"})

def create_app():
    return app

# Vercel serverless function entry point
def main(request):
    return app(request.environ, lambda x, y: None)
