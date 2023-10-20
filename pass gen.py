import string
import random


def generate_random_string(length):
    all_chars = string.printable
    random_string = ''.join(random.choice(all_chars) for _ in range(length))
    return random_string


length = int(input("What is your preferred password length? "))
print(generate_random_string(length))
