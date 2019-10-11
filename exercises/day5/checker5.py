

def check_name(name):
    if not isinstance(name, str):
        print('The given name is not a string!')
        return
    print('Hello '+name)

def check_upper(name):
    if name.upper() == name:
        print('Good!')
    else:
        print(str(name) + 'is not uppercased!')

def check_number(num):
    if not isinstance(num, float):
        print('The given number is not a float!')
        return
    print('Good!')


def check_animals(animals):
    if not isinstance(animals, dict):
        print('The given object is not a dictionary!')
        return
    if 'cats' not in animals or 'dogs' not in animals:
        print('The dictionary does not contain the correct keys!')
        return
    if animals['cats'] != 0 or animals['dogs'] != 0:
        print('The dictionary does not contain the correct values!')
        return
    print('Good!')


def check_animals2(animals):
    if animals['cats'] != 5:
        print('The dictionary does not contain the correct values!')
        return
    print('Good!')

def check_count(num):
    if num != 9:
        print('Not correct!')
        return
    print('Good!')

def check_join(joiner):
    args = ['a','b','c']
    print('a-b-c' == joiner(args))
    print('a_b_c' == joiner(args, '_'))

