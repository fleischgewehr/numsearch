# Numsearch

Computer science task for Evo Summer Python Lab '19. \
This utility allows you to search mobile numbers.

#### Requirements


You need `pytest` to run tests. You can use following command in root directory:

    pip install -r requirements.txt
    
## Usage

You can simply run the `numsearch.py` and enter a phone number. Your input should satisfy
next requirements:
* it starts with '380' following with valid 2-digit mobile operator
* it contains only numbers
* number should be 12 or less digits

Loop will run forever, until you close the program. In this case, you will search
through 25 000 (default value) randomly generated numbers.

To use this script in your own programs, you can do following:

    from numsearch import search_number
    
    my_phonebook: List = [...]  # e.g. ['985553535', '639876543', ...]
    query = '380963'    # sample query number
    
    result = search_number(my_phonebook, query)
    
You can pass list with 9-digit numbers (which start with operator code) as phonebook
argument and any string query that satisfies the above requirements.

#### Testing

To run tests, open your console in root directory and make `pytest numsearch_test.py`.
Make sure you have `pytest` installed on your machine.