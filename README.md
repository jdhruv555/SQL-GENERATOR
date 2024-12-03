# AI SQL Query Generator

A web application that generates SQL queries from natural language descriptions, with support for saving and managing database column descriptions.

## Features
- Natural language to SQL query conversion using Groq's Mixtral model
- Save and manage database schema descriptions
- Simple web interface for query generation
- Support for common SQL operations

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

3. Run the application:
```bash
python app.py
```

## Usage
1. First, add your database schema descriptions through the web interface
2. Enter your query request in plain English
3. Get the generated SQL query instantly

## Note
This application is designed for users familiar with database concepts who want to quickly generate SQL queries using natural language. It uses Groq's Mixtral-8x7b model for high-quality SQL generation.
