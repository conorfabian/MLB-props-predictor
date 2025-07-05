# MLB Props Predictor - Backend

A FastAPI backend application for predicting MLB player props with PostgreSQL database via Supabase.

## Technology Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server for running the FastAPI application
- **Supabase** - Backend-as-a-Service with PostgreSQL database
- **PostgreSQL** - Database for storing player statistics and predictions
- **python-dotenv** - Environment variable management

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Supabase account and project (optional for basic setup)

## Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp env.example .env
   ```
   Edit the `.env` file with your Supabase credentials and configuration.

## Running the Application

### Development Mode

Start the development server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Alternative way to run

You can also run the application using Python directly:
```bash
python main.py
```

## API Documentation

Once the server is running, you can access:

- **Interactive API Documentation (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API Documentation (ReDoc)**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

## Available Endpoints

### Base Endpoints

- `GET /` - Health check endpoint
- `GET /api/bets` - Get MLB betting predictions (placeholder data)

## Project Structure

```
backend/
├── main.py              # FastAPI application entry point
├── database.py          # Database connection and configuration
├── requirements.txt     # Python dependencies
├── env.example         # Example environment variables
├── .env               # Environment variables (create this file)
└── README.md          # This file
```

## Environment Variables

Create a `.env` file in the backend directory with the following variables:

```env
# Supabase configuration
SUPABASE_URL=your_supabase_url_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
SUPABASE_ANON_KEY=your_anon_key_here

# Database configuration
DATABASE_URL=postgresql://username:password@host:port/database_name

# App configuration
DEBUG=True
SECRET_KEY=your_secret_key_here
```

## Database Setup

1. Create a Supabase project at [supabase.com](https://supabase.com)
2. Get your project URL and API keys from the Supabase dashboard
3. Update the `.env` file with your Supabase credentials
4. Use the `database.py` file to interact with your Supabase database

## CORS Configuration

The application is configured to allow requests from:
- `http://localhost:5173` (React development server)

To add more origins, update the `allow_origins` list in `main.py`.

## Development

### Installing New Dependencies

When adding new dependencies:

1. Install the package:
   ```bash
   pip install package_name
   ```

2. Update requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

### Running Tests

(Tests will be added in future iterations)

## Notes

- The server runs on port 8000 by default
- CORS is configured to allow requests from the React frontend
- Environment variables are loaded automatically via python-dotenv
- The API uses async/await for better performance 