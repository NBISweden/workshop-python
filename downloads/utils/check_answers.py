"""
Usage: Input filename of sequence to compare against correct reference sequence.
       One function for each exercise.
"""

import urllib.request

def compare(infile, correctFile):
    url      = correctFile
    response = urllib.request.urlopen(url)
    data     = response.read().strip()
    correct  = data.decode('utf-8')

    # check the previous output compared to correct file
    fh  = open(infile, 'r')

    test    = []
    for line in fh:
        test.append(line.strip())

    correct = ''.join(correct)
    test    = ''.join(test)

    if not len(test) == len(correct):
        print('The sequences are of different length, try again')
        return True

    i = 0
    while i < len(correct):
        if not correct[i].lower() == test[i].lower():
            print('Not matching at pos '+str(i))
            return True
        else:
            pass
        i += 1
    print('The sequences are matching!')
    return True


def ex3(infile):
  """
   Usage: Input filename of output from exercise 3
  """
  compare(infile, 'https://raw.githubusercontent.com/NBISweden/PythonCourse/ht19/assignment/results/transcript.ncbi.fasta')


def ex4(infile):
  """
   Usage: Input filename of output from exercise 4
  """
  compare(infile, 'https://raw.githubusercontent.com/NBISweden/PythonCourse/ht19/assignment/results/mrna.ncbi.fasta')


def ex6(infile):
  """
   Usage: Input filename of output from exercise 6
  """
  compare(infile, 'https://raw.githubusercontent.com/NBISweden/PythonCourse/ht19/assignment/results/protein.ncbi.fasta')
