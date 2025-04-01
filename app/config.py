from decouple import config, Csv

# Application Settings
DEBUG = config('DEBUG', default=False, cast=bool)
ECHO_ACTIVE = config('ECHO_ACTIVE', default=1, cast=int)





ENVIRONMENT = config('ENVIRONMENT', default='development')

# Server Settings
HOST = config('HOST', default='0.0.0.0')
PORT = config('PORT', default=8000, cast=int)
WORKERS = config('WORKERS', default=4, cast=int)
LOG_LEVEL = config('LOG_LEVEL', default='info')

# Database Settings
DATABASE_URL = config('DATABASE_URL', default='sqlite:///./sql_app.db')

# Security
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM', default='HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES', default=30, cast=int)

# CORS
ALLOWED_ORIGINS = config('ALLOWED_ORIGINS', default='http://localhost:3000,http://localhost:8000', cast=Csv())