import random
import string

def generate_password(length, use_special_chars=True):
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''
    
    
    all_chars = letters + digits + special_chars
    
    
    if length <= 0 or length > len(all_chars):
        raise ValueError("Password length must be between 1 and the number of available characters.")
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    try:
        
        length = int(input("Enter the desired length of the password: "))
        
        
        use_special_chars = input("Include special characters (y/n)? ").strip().lower() == 'y'
        
        
        password = generate_password(length, use_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
if __name__ == "__main__":
    main()