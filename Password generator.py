import string
import random

def gen_pw(length,complexity):
    if complexity == "weak":
        chars = string.ascii_letters 
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits 
    elif complexity == "strong":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level")
        
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password:"))
            if length <= 0:
                raise ValueError("Password length should be greater than 0.")

            complexity = input("Enter the complexity level (weak, medium, strong) : ").lower()
            if complexity not in ["weak", "medium", "strong"]:
                raise ValueError("Complexity level should be 'weak', 'medium', or 'strong'.")
                
        except ValueError as ve:
            print("Invalid input:",ve)
            return
            
        password = gen_pw(length,complexity)
        print("Generated Password : ",password)
        ask = input("Do you want another password> (Y/N) : ").lower()
        if ask != 'y':
            break

if __name__ == "__main__":
    main()

    
