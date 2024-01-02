import os
import re

def filter_passwords(file_path, min_uppercase, min_lowercase, min_special, min_numbers, min_total_chars):
    with open(file_path, 'r') as file:
        passwords = file.readlines()

    filtered_passwords = []

    for password in passwords:
        # Count the occurrences of each character type
        uppercase_count = sum(1 for char in password if char.isupper())
        lowercase_count = sum(1 for char in password if char.islower())
        special_count = sum(1 for char in password if not char.isalnum())
        numbers_count = sum(1 for char in password if char.isdigit())

        # Check if the password meets the criteria
        if (
            uppercase_count >= min_uppercase and
            lowercase_count >= min_lowercase and
            special_count >= min_special and
            numbers_count >= min_numbers and
            len(password) >= min_total_chars
        ):
            filtered_passwords.append(password.strip())

    return filtered_passwords

def main():
    # Get user input
    file_path = input("Enter the full path to the list file: ")
    
    min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
    min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
    min_special = int(input("Enter the minimum number of special characters: "))
    min_numbers = int(input("Enter the minimum number of numbers: "))
    min_total_chars = int(input("Enter the minimum total number of characters: "))

    # Filter passwords based on user input
    filtered_passwords = filter_passwords(file_path, min_uppercase, min_lowercase, min_special, min_numbers, min_total_chars)

    # Print the results
    print("\nFiltered Passwords:")
    for password in filtered_passwords:
        print(password)

if __name__ == "__main__":
    main()
