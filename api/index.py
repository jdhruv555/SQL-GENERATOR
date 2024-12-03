from flask import Flask, request, jsonify, render_template
from groq import Groq
from dotenv import load_dotenv
import os
import json
from pathlib import Path

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='../templates')

# Copy all your existing route handlers from app.py here
# (Paste the entire content of your current app.py)

@app.route('/')
def home():
    return render_template('index.html')

# Vercel requires a specific handler
def create_app():
    return app

# For Vercel serverless functions
def handler(event, context):
    return app
