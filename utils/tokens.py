import secrets
from datetime import datetime, timedelta
from typing import Optional
import jwt
from decouple import config

# Load configuration
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM', default='HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES', default=30, cast=int)

def generate_secret_key(length: int = 32) -> str:
    """
    Generate a secure random secret key.

    Args:
        length: Length of the key in bytes (default: 32)

    Returns:
        str: A secure random string
    """
    return secrets.token_hex(length)

def generate_api_key(length: int = 32) -> str:
    """
    Generate a secure API key.

    Args:
        length: Length of the key in bytes (default: 32)

    Returns:
        str: A secure API key
    """
    return secrets.token_urlsafe(length)

def generate_verification_token(length: int = 32) -> str:
    """
    Generate a secure verification token.

    Args:
        length: Length of the token in bytes (default: 32)

    Returns:
        str: A secure verification token
    """
    return secrets.token_urlsafe(length)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token.

    Args:
        data: Data to encode in the token
        expires_delta: Optional expiration time delta

    Returns:
        str: JWT token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict:
    """
    Verify a JWT token.

    Args:
        token: JWT token to verify

    Returns:
        dict: Decoded token data

    Raises:
        jwt.PyJWTError: If token is invalid
    """
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])