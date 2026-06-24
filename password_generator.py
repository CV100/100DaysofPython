# Password generator

# Uppercase and lowercase letters
import random

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Numbers
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

# Common symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~'
]

length_psw = int(input("How long shall the password be?: "))
number_nums = int(input("How many numbers would you like?: "))
number_symbols = int(input("How many symbols would you like?: "))

temporary_password = []
final_password = ""

for letter in range(1, length_psw + 1):
    the_letter = random.choice(letters)
    temporary_password += the_letter

for number in range (1, number_nums + 1):
    the_number = random.choice(numbers)
    temporary_password += the_number

for symbol in range(1, number_symbols + 1):
    the_symbol = random.choice(symbols)
    temporary_password += the_symbol

print(temporary_password)

for password in range(1, len(temporary_password) + 1):
    the_password = random.choice(temporary_password)
    idx = temporary_password.index(the_password)
    if the_password in temporary_password:
        temporary_password.pop(idx)
    final_password += the_password

print(final_password)


