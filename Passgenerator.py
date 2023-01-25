import random
import string


def generate_password():

    set_password_length = random.randint(8, 24)
    ascii_letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    
    expected_characters = ascii_letters + digits + special_characters

    password = "".join(
        random.choice(expected_characters) for i in range(set_password_length))

    return password

print(generate_password())
