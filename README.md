# FastAPI Image Processing Service

A modern web service built with FastAPI that handles image processing and authentication.

> This project was built following the excellent [FastAPI tutorial by CodingForEntrepreneurs](https://www.youtube.com/watch?v=JxH7cdDCFwE) with additional customizations and features.

## Features

- 🚀 Fast and async API endpoints
- 🔐 Secure token-based authentication
- 🖼️ Image processing capabilities
- 📝 OCR text extraction
- 🔒 Environment-based configuration
- 🐋 Docker support

## Concepts Implemented

- 🎨 FastAPI & Jinja Templates for dynamic web pages
- 🧪 FastAPI & PyTest Integration for robust testing
- 🔄 Git Workflow & Pre-commit Hooks for code quality
- 🚀 DigitalOcean Deployment strategies
- 🐳 Docker App Deployment
- ⚙️ Settings, Environment Variables & dotenv configuration
- 📤 File Upload Handling
- ✅ Automated Testing for File Uploads
- 🖼️ Image Upload Validation & Tests
- 📝 Tesseract & pytesseract Integration for OCR
- 🔐 Authorization Headers for security
- 🌐 Production Endpoint & Auth Testing
- 🎯 One-Click Deployment Setup

## Prerequisites

- Python 3.12+
- Tesseract OCR
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ms-fastapi.git
cd ms-fastapi
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
cp .env.example .env
```

5. Generate a secret key:
```bash
python scripts/generate_secret.py
```

## Development

Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## Docker Deployment

Build and run with Docker:
```bash
docker build -t ms-fastapi .
docker run -p 8000:8000 ms-fastapi
```

## API Endpoints

- `GET /` - Home page
- `POST /` - Echo endpoint
- `POST /img-echo/` - Image processing endpoint

## Authentication

Generate authentication tokens:
```bash
python scripts/token_generator.py --type jwt --data "user@example.com" --secret-key "your-secret" --expires 30
```

Token types:
- Secret keys
- API keys
- Verification tokens
- JWT tokens

## Testing

Run tests with pytest:
```bash
pytest
```

Pre-commit hooks are configured for:
- Code formatting
- YAML validation
- Large file checks
- Automated testing

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DEBUG | Debug mode | False |
| ECHO_ACTIVE | Enable echo endpoint | 1 |
| HOST | Server host | 0.0.0.0 |
| PORT | Server port | 8000 |
| SECRET_KEY | JWT secret key | Required |
| ALGORITHM | JWT algorithm | HS256 |

