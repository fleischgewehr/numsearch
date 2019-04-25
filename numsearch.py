from random import randint, choice
from itertools import islice
import re

OPERATOR = [
    '67', '96', '97', '98', '50',
    '66', '95', '99', '63', '73',
    '93', '91', '92', '94',
]


def generate_phonebook(quantity=25000):
    """
    Generating random phone numbers.

    There is no country code ('380') in numbers,
    because it's redundant after user input validation.
    It also makes searching a bit faster.
    """
    return [choice(OPERATOR) + str(randint(1000000, 9999999))
            for _ in range(quantity)]


def search_number(phonebook, user_num):
    """
    Get user input and search for numbers in the phonebook.
    """
    if 3 < len(user_num) <= 12 and re.match(
            r'^380(67|96|97|98|50|66|95|99|63|73|93|91|92|94|5$|6$|7$|9$)[0-9]*$',
            user_num):
        pure = user_num[3:]  # removes country code ('380')

        generator = ('380' + num for num in phonebook
                     if pure == num[:len(pure)])
        # islice stops iterating when we reach 10 results
        return list(islice(generator, 10))

    # if user entered less or equal than 3 digits (which are '380')
    # we return first 10 phone numbers, because input fits every number
    elif len(user_num) <= 3 and re.match(r'\A(380|38|3)$', user_num):
        return ['380' + num for num in phonebook[:10]]

    else:
        return 'No matches. Make sure your number is valid (e.g. "380985553535").'


if __name__ == '__main__':
    phonebook = generate_phonebook()

    while True:
        user_num = input('Enter a phone number: ')
        print(f'Result: {search_number(phonebook, user_num)}')
