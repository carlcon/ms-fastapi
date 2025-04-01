from utils.tokens import generate_secret_key

def main():
    # Generate a secure secret key
    secret_key = generate_secret_key()

    print("\nGenerated Secret Key:")
    print(f"SECRET_KEY={secret_key}")
    print("\nCopy this key to your .env file")
    print("Make sure to keep it secure and never commit it to version control!")

if __name__ == "__main__":
    main()