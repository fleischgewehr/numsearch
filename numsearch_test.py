from numsearch import generate_phonebook, search_number


def test_generator():
    assert len(generate_phonebook()) == 25000
    assert len(generate_phonebook(10000)) == 10000


def test_search():
    phonebook = generate_phonebook()
    WARNING_ = 'No matches. Make sure your number is valid (e.g. "380985553535").'

    # invalid country code
    assert search_number(phonebook, '780') == WARNING_
    assert search_number(phonebook, '390') == WARNING_
    assert search_number(phonebook, '389') == WARNING_
    assert search_number(phonebook, '792') == WARNING_

    # make sure we get 10 numbers
    assert len(search_number(phonebook, '380')) == 10

    # make sure we get first 10 numbers when length of
    # user input is less than 4 and it's country code
    assert [num[3:] for num in search_number(phonebook, '380')] == phonebook[:10]
    assert [num[3:] for num in search_number(phonebook, '38')] == phonebook[:10]
    assert [num[3:] for num in search_number(phonebook, '3')] == phonebook[:10]

    # invalid mobile operator
    assert search_number(phonebook, '3804') == WARNING_
    assert search_number(phonebook, '38090') == WARNING_

    # letters in user input
    assert search_number(phonebook, '380988f') == WARNING_
    assert search_number(phonebook, '380987b3') == WARNING_

    # too long number
    assert search_number(phonebook, '3809655535351') == WARNING_
