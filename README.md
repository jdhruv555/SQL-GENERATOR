# AI SQL Query Generator

## Deployment

### Vercel Deployment

1. Fork the repository
2. Connect your GitHub repository to Vercel
3. Set environment variables:
   - `GROQ_API_KEY`: Your Groq API key
   - `PYTHON_VERSION`: 3.9 or 3.10

### Local Development

1. Clone the repository
2. Create a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables
   ```bash
   cp .env.example .env
   # Edit .env with your Groq API key
   ```
5. Run the application
   ```bash
   flask run
   ```

## Features

- Natural language to SQL query conversion
- AI-powered query generation
- Responsive web interface
- Dynamic schema management

## Technologies

- Flask
- Groq API
- Tailwind CSS
- Python 3.9+

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed changes.

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
