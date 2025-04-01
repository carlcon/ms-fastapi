#!/usr/bin/env python3
import argparse
import secrets
from datetime import datetime, timedelta
import jwt
from typing import Optional

def generate_secret_key(length: int = 32) -> str:
    """Generate a secure random secret key."""
    return secrets.token_hex(length)

def generate_api_key(length: int = 32) -> str:
    """Generate a secure API key."""
    return secrets.token_urlsafe(length)

def generate_verification_token(length: int = 32) -> str:
    """Generate a secure verification token."""
    return secrets.token_urlsafe(length)

def create_jwt_token(
    data: str,
    secret_key: str,
    algorithm: str = "HS256",
    expires_minutes: Optional[int] = None
) -> str:
    """Create a JWT token."""
    payload = {"data": data}
    if expires_minutes:
        payload["exp"] = datetime.utcnow() + timedelta(minutes=expires_minutes)
    return jwt.encode(payload, secret_key, algorithm=algorithm)

def main():
    parser = argparse.ArgumentParser(description="Generate secure tokens")
    parser.add_argument(
        "--type",
        choices=["secret", "api", "verify", "jwt"],
        required=True,
        help="Type of token to generate"
    )
    parser.add_argument(
        "--length",
        type=int,
        default=32,
        help="Length of the token in bytes (default: 32)"
    )
    parser.add_argument(
        "--data",
        help="Data to encode in JWT token (required for JWT type)"
    )
    parser.add_argument(
        "--secret-key",
        help="Secret key for JWT token (required for JWT type)"
    )
    parser.add_argument(
        "--expires",
        type=int,
        help="Expiration time in minutes for JWT token"
    )

    args = parser.parse_args()

    if args.type == "secret":
        token = generate_secret_key(args.length)
        print(f"\nGenerated Secret Key:")
        print(f"SECRET_KEY={token}")
    elif args.type == "api":
        token = generate_api_key(args.length)
        print(f"\nGenerated API Key:")
        print(f"API_KEY={token}")
    elif args.type == "verify":
        token = generate_verification_token(args.length)
        print(f"\nGenerated Verification Token:")
        print(f"TOKEN={token}")
    elif args.type == "jwt":
        if not args.data or not args.secret_key:
            parser.error("--data and --secret-key are required for JWT tokens")
        token = create_jwt_token(
            args.data,
            args.secret_key,
            expires_minutes=args.expires
        )
        print(f"\nGenerated JWT Token:")
        print(f"JWT_TOKEN={token}")

    print("\nMake sure to keep these tokens secure and never commit them to version control!")

if __name__ == "__main__":
    main()