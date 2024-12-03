from flask import Flask, request, jsonify, render_template
from groq import Groq
from dotenv import load_dotenv
import os
import json
from pathlib import Path

# Load environment variables
load_dotenv()

app = Flask(__name__)
groq_client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# File to store column descriptions
SCHEMA_FILE = 'schema_descriptions.json'

def load_schema_descriptions():
    if Path(SCHEMA_FILE).exists():
        with open(SCHEMA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_schema_descriptions(descriptions):
    with open(SCHEMA_FILE, 'w') as f:
        json.dump(descriptions, f, indent=2)

def generate_sql_query(query_description, schema_descriptions):
    # Construct the prompt with schema information
    schema_context = "\n".join([
        f"Table/Column: {name}, Description: {desc}"
        for name, desc in schema_descriptions.items()
    ])
    
    prompt = f"""Given the following database schema descriptions:
{schema_context}

Generate a SQL query for this request: {query_description}

Return only the SQL query without any explanations."""

    completion = groq_client.chat.completions.create(
        model="mixtral-8x7b-32768",  # Using Mixtral model for better performance
        messages=[
            {"role": "system", "content": "You are a SQL expert. Generate precise SQL queries based on natural language descriptions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1  # Lower temperature for more precise SQL generation
    )
    
    return completion.choices[0].message.content.strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/schema', methods=['GET', 'POST'])
def manage_schema():
    if request.method == 'POST':
        data = request.json
        descriptions = load_schema_descriptions()
        descriptions.update(data)
        save_schema_descriptions(descriptions)
        return jsonify({"status": "success"})
    else:
        return jsonify(load_schema_descriptions())

@app.route('/api/generate', methods=['POST'])
def generate_query():
    data = request.json
    query_description = data.get('description')
    schema_descriptions = load_schema_descriptions()
    
    try:
        sql_query = generate_sql_query(query_description, schema_descriptions)
        return jsonify({"query": sql_query})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
