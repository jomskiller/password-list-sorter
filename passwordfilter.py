import os

def filter_passwords(file_path, min_uppercase, min_lowercase, min_special, min_numbers, min_total_chars):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            passwords = file.readlines()
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []

    filtered_passwords = []

    for password in passwords:
        # Count the occurrences of each character type
        uppercase_count = sum(1 for char in password if char.isupper())
        lowercase_count = sum(1 for char in password if char.islower())
        special_count = sum(1 for char in password if not char.isalnum() and not char.isspace())
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

def save_to_file(filtered_passwords, output_file_path):
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(password + '\n' for password in filtered_passwords)

def get_user_input(prompt):
    return input(prompt).strip()

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    # Print a cool ASCII art banner
    print("""
 .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |     _____    | | |     ____     | | | ____    ____ | | |    _______   | | |  ___  ____   | | |     _____    | | |   _____      | | |   _____      | | |  _________   | | |  _______     | |
| |    |_   _|   | | |   .'    `.   | | ||_   \  /   _|| | |   /  ___  |  | | | |_  ||_  _|  | | |    |_   _|   | | |  |_   _|     | | |  |_   _|     | | | |_   ___  |  | | | |_   __ \    | |
| |      | |     | | |  /  .--.  \  | | |  |   \/   |  | | |  |  (__ \_|  | | |   | |_/ /    | | |      | |     | | |    | |       | | |    | |       | | |   | |_  \_|  | | |   | |__) |   | |
| |   _  | |     | | |  | |    | |  | | |  | |\  /| |  | | |   '.___`-.   | | |   |  __'.    | | |      | |     | | |    | |   _   | | |    | |   _   | | |   |  _|  _   | | |   |  __ /    | |
| |  | |_' |     | | |  \  `--'  /  | | | _| |_\/_| |_ | | |  |`\____) |  | | |  _| |  \ \_  | | |     _| |_    | | |   _| |__/ |  | | |   _| |__/ |  | | |  _| |___/ |  | | |  _| |  \ \_  | |
| |  `.___.'     | | |   `.____.'   | | ||_____||_____|| | |  |_______.'  | | | |____||____| | | |    |_____|   | | |  |________|  | | |  |________|  | | | |_________|  | | | |____| |___| | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' 
    """)

    # Get user input
    file_path = get_user_input("Enter the full path to the list file: ")
    
    min_uppercase = get_integer_input("Enter the minimum number of uppercase letters: ")
    min_lowercase = get_integer_input("Enter the minimum number of lowercase letters: ")
    min_special = get_integer_input("Enter the minimum number of special characters: ")
    min_numbers = get_integer_input("Enter the minimum number of numbers: ")
    min_total_chars = get_integer_input("Enter the minimum total number of characters: ")

    # Filter passwords based on user input
    filtered_passwords = filter_passwords(file_path, min_uppercase, min_lowercase, min_special, min_numbers, min_total_chars)

    if not filtered_passwords:
        return

    # Save the results to a file
    output_file_path = get_user_input("Enter the full path for the output file: ")
    save_to_file(filtered_passwords, output_file_path)

    print(f"\nFiltered Passwords saved to {output_file_path}")

if __name__ == "__main__":
    main()
