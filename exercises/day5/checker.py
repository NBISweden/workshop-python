
def runner(func):
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
    return 'Hello '+name

@runner
def check_upper(name):
    assert name.upper() == name, '{} is not uppercased!'.format(name)

@runner
def check_number(num):
    assert isinstance(num, float), 'The given number is not a float!'


@runner
def check_animals(animals):
    assert isinstance(animals, dict), \
        'The given object is not a dictionary!'
    assert 'cats' in animals and 'dogs' in animals, \
        'The dictionary does not contain the correct keys!'
    assert animals['cats'] == 1 and animals['dogs'] == 1, \
        'The dictionary does not contain the correct values!'


@runner
def check_animals2(animals):
    assert animals['cats'] == 5, \
        'The dictionary does not contain the correct values!'

@runner
def check_animal_choice(choice):
    assert choice in [5, 1], \
        '{} is not the value of either cat or dog'.format(choice)
    animal = 'dogs' if choice == 1 else 'cats'
    return 'Yes, you can handle dictionaries and you like {}!'.format(animal)


@runner
def check_appended(result):
    assert result == "snake", "You created the string {}, that's not correct".format(result)

@runner
def check_count(num):
    assert num == 9, "You counted {} 'a's, that's not correct".format(num)


@runner
def check_join(joiner):
    args = ['a','b','c']
    assert 'abc' == joiner(args), 'The joining went wrong'
    # assert 'a_b_c' == joiner(args, '_'), 'The joining went wrong'


@runner
def check_average(l, s, a):
    assert l == 33
    assert s == 97
    assert a == 97/33

@runner
def check_file(data):
    cat = " /\\_/\\\\n( ^.^ )\\n > U <"
    dog = "(\,--------'()'--o\\n (_    ___    /~\"\\n (_)_)  (_)_)"
    assert isinstance(data, str), 'Did you open and read the file corretly? The output is not a string'
    # Check if the beginning of the string is correct, avoid the newlines
    assert data[:10] in [cat[:10], dog[:10]], 'The data you read is incorrect'


@runner
def check_replace(text):
    assert text == 'python', 'The text is still "{}"'.format(text)

@runner
def check_lastvalue(coded):
    assert coded[1] == 'programmer', 'String at position 1 is wrong'


@runner
def check_remmagorp(coded):
    assert coded == 'programmer', 'You got {}, that\'s not correct'

@runner
def check_dog(word):
    assert word == 'is', '"{}" is not the correct word'.format(word)


@runner
def check_splitted(splitted):
    assert splitted == ['python', 'remmargorp'], 'The splitting did not work!'


def check():
    print('It works!')


@runner
def check_snakes(snake):
    assert snake == 'python', '{} is not the correct answer!'.format(snake)

@runner
def check_maybe(maybe):
    assert maybe == 'is', '{} is not the correct answer!'.format(maybe)

x = 77

