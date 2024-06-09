import string
import random

def gen_pw(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password:"))
        if length <= 0:
            raise ValueError("Password length should be greater than 0.")
    except ValueError as ve:
        print("Invalid input:",ve)
        return
    
    password = gen_pw(length)

    print("Generated Password : ",password)

if __name__ == "__main__":
    main()

    