import random
import re


# TODO Hints

exercises = [
   (['abc', 'abcd', 'abcde'], ['xyz', 'def'], "Look at the beginning of the strings. Remember how to match everything?"),
   (['abc', 'abbbc', 'abbbbc'], ['ac'], "How many b's do you need to accept?"),
   (['b', 'abbbc', 'abbbbc'], ['ac'], "What letter is common to all good examples?"),
   (['abc', 'adc', 'axc'], ['abe', 'ay'], "There seems to be only one position that may vary"),
   (['abc', 'ac'], ['abbc'], "How many b's?"),
   # .*\s.*
   (['a bc', 'a c d'], ['abbc'], "There are whitespaces here!"),
   (['cat', 'hat'], ['sat', 'rat', 'mat', 'at', 'gat'], "Remeber how to allow a set of characters?"),
   (['sat', 'rat', 'mat', 'gat', 'hat'], ['cat'], "Remeber how to disalllow a set of characters?"),
   (['barn', 'grain', 'brat', 'sorry'], ['ban', 'gain', 'bat', 'soy'], "What character is common to all good examples?"),
   (['dogs', 'cats', 'horses'], ['dog', 'cat', 'mice', 'cow'], "There's something in the end..."),
   (['karlsson', 'carlson', 'carlzon', 'karlson'], ['larsson', 'karl', 'carlo'], "If you're lazy, just look at the beginning and the end"),
   (['vision', 'explosion', 'fusion'], ['station', 'motion', 'region'], "Any start will do..."),
   (['ATG', 'ATA', 'ATT'], ['AAG', 'AGA', 'ACT'], "."),
   (['words', 'letters', 'text'], ['not word', 'åå', 'work-shop', '88'], "Only the english alphabet is allowed here"),
   (['88', '337', '0'], ['elephant', 'two', '.99', '-22'], "Digits!"),
]


def test(pattern, expr):
    goods, bads, help = expr
    p = re.compile('^'+pattern+'$')
    for good in goods:
        if p.search(good) is None:
            print('failed', good)
            print('Try again!')
            return False
    for bad in bads:
        if p.search(bad) is not None:
            print('failed', bad)
            print('Try again!')
            return False
    ok = ['Well done!', 'Good job!', 'Excellent!', 'Great!']
    print(random.choice(ok))
    return True


if __name__ == "__main__":
    print('Hello!\nFor each given example, write a pattern that matches the Accept strings',
          'and that doesn\'t match the Reject string. Then press Enter.',
          '\nType "help" to get a hint or "skip" to skip the current question.',
          '\nTo exit, type Ctrl+c\n')
    for ex in exercises:
        didit = False
        while not didit:
            print('Accept {}'.format(', '.join(ex[0])))
            print('Reject {}'.format(', '.join(ex[1])))
            pattern = input('> ').strip()
            if pattern == "help":
                print('Hint:', ex[2])
                pattern = input('> ')
            if pattern == "skip":
                didit = True
                continue
            didit = test(pattern, ex)
            print()
