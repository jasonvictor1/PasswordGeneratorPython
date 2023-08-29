# Import the random module to generate random values
import random

def generate_strong_password(desired_length=8):
    # Define sets of characters to be used for generating the password
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%^&*()_-+=<>?/:;{}[]|"
    numbers = "0123456789"
    password = ""

    # Determine the password length based on user input, defaulting to 8 characters if not specified
    if desired_length > 8:
        length = desired_length
    else:
        length = 8

    # Ensure that the generated password contains at least one character from each category
    password += random.choice(uppercase_letters)  # Add a random uppercase letter
    password += random.choice(lowercase_letters)  # Add a random lowercase letter
    password += random.choice(special_characters) # Add a random special character
    password += random.choice(numbers)           # Add a random number

    # Calculate the number of characters remaining to reach the desired password length
    remaining_length = length - 4

    # Create a pool of characters containing all possible characters
    character_pool = uppercase_letters + lowercase_letters + special_characters + numbers

    # Generate the remaining characters for the password
    for count in range(remaining_length):
        random_character = random.choice(character_pool)
        password += random_character

    # Shuffle the characters in the password to randomize the order
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = "".join(password_list)

    # Return the generated password
    return shuffled_password

# Option 1 - Password Strengthener with Fixed Length (8 characters)
generated_password_1 = generate_strong_password()
print("Generated Password (8 characters):", generated_password_1)

# Option 2 - Password Strengthener with Customizable Length
while True:
    try:
        desired_length_2 = int(input("Enter desired password length (customized length): "))
        if desired_length_2 < 8:
            print("Password length must be at least 8 characters.")
        else:
            break
    except ValueError:
        # Catch the ValueError exception if user enters a non-integer value for desired_length_2
        print("Invalid input. Please enter an integer.")

# Generate the password with the user-specified length
generated_password_2 = generate_strong_password(desired_length_2)
print("Generated Password (customized length):", generated_password_2)
