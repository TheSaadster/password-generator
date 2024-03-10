import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = has_special and meets_criteria
    return password

min_length = 0
while min_length <= 0:
    try:
        min_length = int(input("Enter the minimum length of the password: "))
        if min_length <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a number that is greater than zero.")
    
    
has_numbers = input("Do you want numbers in your password? (y/n): ").lower() == "y"
has_special_characters = input("Do you want special characters in your password? (y/n): ").lower() == "y"


password = generate_password(min_length, has_numbers, has_special_characters)
print("The generated password is:", password)
