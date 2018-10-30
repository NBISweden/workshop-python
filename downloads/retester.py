"""
Module for testing regex pattern.
Usage: python3 retester.py
"""
import os
import random
import re
import readline


# All exercises
exercises = [
    (['abc', 'abcd', 'abcde'], ['xyz', 'def'], "Look at the beginning of the strings. Remember how to match everything?"),
    (['abc', 'abbbc', 'abbbbc'], ['ac'], "How many b's do you need to accept?"),
    (['b', 'abbbc', 'abbbbc'], ['ac'], "What letter is common to all good examples?"),
    (['abc', 'adc', 'axc'], ['abe', 'ay'], "There seems to be only one position that may vary"),
    (['abc', 'ac'], ['abbc'], "How many b's?"),
    (['a bc', 'a c d'], ['abbc'], "There are whitespaces here!"),
    (['cat', 'hat'], ['sat', 'rat', 'mat', 'at', 'gat'], "Remeber how to allow a set of characters?"),
    (['sat', 'rat', 'mat', 'gat', 'hat'], ['cat'], "Remeber how to disalllow a set of characters?"),
    (['barn', 'grain', 'brat', 'sorry'], ['ban', 'gain', 'bat', 'soy'], "What character is common to all good examples?"),
    (['dogs', 'cats', 'horses'], ['dog', 'cat', 'mice', 'cow'], "There's something in the end..."),
    (['karlsson', 'carlson', 'carlzon', 'karlson'], ['larsson', 'karl', 'carlo'], "If you're lazy, just look at the beginning and the end"),
    (['vision', 'explosion', 'fusion'], ['station', 'motion', 'region'], "Any start will do..."),
    (['TAG', 'TAA', 'TGA'], ['TCG', 'AGA', 'ACT'], "Mind the case! T != t"),
    (['words', 'letters', 'text'], ['not word', 'åå', 'work-shop', '88'], "Only the english alphabet is allowed here"),
    (['88', '337', '0'], ['elephant', 'two', '.99', '-22'], "Digits!"),
]


def test(pattern, expr):
    """
    Test if a pattern matches the positive examples and reject the negative
    """
    goods, bads, hint = expr
    try:
        p = re.compile('^'+pattern+'$')
    except re.error:
        print("Invalid regular expression. Try again!")
        return False
    for good in goods:
        if p.search(good) is None:
            print('Failed. Did not match the string {!r} which should be accepted'.format(good))
            print('Try again!')
            return False
    for bad in bads:
        if p.search(bad) is not None:
            print('Failed. Matched the string {!r} which should be rejected'.format(bad))
            print('Try again!')
            return False
    ok = ['Well done!', 'Good job!', 'Excellent!', 'Great!']
    return random.choice(ok)


def ask_question(exercise):
    """
    Print the examples and get the user input
    """
    print('Accept {}'.format(', '.join('{!r}'.format(e) for e  in exercise[0])))
    print('Reject {}'.format(', '.join('{!r}'.format(e) for e  in exercise[1])))
    return input('> ').strip()


def main():
    """
    The main loop
    """
    didit = False
    for ex in exercises:
        if didit:
            print(didit)
            print()
            print('Next exercise:')
        didit = False
        while not didit:
            pattern = ask_question(ex)
            if pattern == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                pattern = ask_question(ex)
            if pattern == "help":
                print('Hint:', ex[2])
                pattern = input('> ').strip()
            if pattern == "skip":
                didit = True
                continue
            didit = test(pattern, ex)


if __name__ == "__main__":
    readline.parse_and_bind('set editing-mode vi')
    print('Hello!\nFor each given example, write a regular expression that matches the Accept strings',
          'and that doesn\'t match the Reject string. Then press Enter.',
          '\nType "help" to get a hint or "skip" to skip the current question.',
          '\nType "clear" to get clear the terminal screen.',
          '\nTo exit, type Ctrl+c\n')
    main()
    print('Good work! You\'re done!\nBye!\n')
