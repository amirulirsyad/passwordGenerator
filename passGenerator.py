import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            print("Please enter a positive integer for the password length.")
        else:
            password = generate_password(password_length)
            print(f"Your randomly generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
