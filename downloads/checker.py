"""This file contains help and check functions for the course quiz."""


def runner(func):
    """A decorator for printing results."""
    def wrapper(*args):
        try:
            out = func(*args)
        except AssertionError as a:
            print('Oops! something went wrong!')
            print(a)
            return
        print(out or 'Correct!')
    return wrapper


@runner
def check_name(name):
    assert isinstance(name, str), 'The given name is not a string!'
    assert name.strip(), 'That string is empty.'
    return 'Hello '+name


@runner
def check_number(num):
    assert isinstance(num, float), 'The given number is not a float!'
    assert num == 5.0 , '{} is not the correct number'.format(num)


@runner
def check_animals(animals):
    assert isinstance(animals, dict), \
        'The given object is not a dictionary!'
    assert 'snake' in animals and 'bird' in animals, \
        'The dictionary does not contain the correct keys!'
    assert animals['snake'] == '' and animals['bird'] == '', \
        'The dictionary does not contain the correct values!'


@runner
def check_animals2(animals):
    assert animals['snake'] == "python", \
        'The dictionary does not contain the correct values!'


@runner
def check_snake(choice):
    assert choice == "python", \
        'The value should be python, but it is {}'.format(choice)


@runner
def check_word(result):
    assert result.lower() == "programmer", \
        "You created the string {}, that's not correct".format(result)


@runner
def check_average(length, sum, average):
    assert length == 33, '{} is not the correct length'.format(length)
    assert sum == 97, '{} is not the correct sum'.format(sum)
    assert average == 97/33, '{} is not the correct average'.format(average)


def check():
    print('It works!')


@runner
def check_snakes(snake):
    assert snake == 'python', '{} is not the correct answer!'.format(snake)


@runner
def check_maybe(maybe):
    assert maybe == 'is', '{} is not the correct answer!'.format(maybe)


@runner
def final(output):
    result = 'is a python programmer!'.split()
    vars = "{maybeis} {chr(the_sum)} {the_snake} {word}{chr(the_length)}".split()
    errs = []
    for corr, word, var in zip(result, output.split()[1:], vars):
        if corr != word:
            errs.append('the value for "{}" is "{}", which does not seem correct'.format(var, word))
    assert not errs, '\n'.join(errs)
    return "You passed the test! Congratulations!"

# to be used in the if statement
x = 77
