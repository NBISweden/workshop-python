#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from functools import wraps

def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        retval = func(*args, **kwargs)
        end = time.time()
        print("Time for %s: %.2f seconds" % (func.__qualname__,end-start))
        return retval
    return wrapper


# http://www2.sluh.org/bioweb/bi100/tutorials/thegeneticcode/codonwheel2.jpg
# https://en.wikipedia.org/wiki/Protein_primary_structure

from pprint import pprint

_debug = False

class RNATranslationTableBase():
    _store = None
    def print(self):
        pprint(self._store)

class RNATranslationTable(RNATranslationTableBase):
    _store = {
        'G': {
            'G': { # Glycine (Gly)
                'G': 'G',
                'U': 'G',
                'C': 'G',
                'A': 'G'
            },
            'U': { # Valine (Val)
                'G': 'V',
                'U': 'V',
                'C': 'V',
                'A': 'V'
            },
            'C': { # Alanine (Ala)
                'G': 'A',
                'U': 'A',
                'C': 'A',
                'A': 'A'
            },
            'A': {
                'G': 'E', # Glutamic acid (Glu)
                'U': 'D', # Aspartic acid (Asp)
                'C': 'D', # Asp
                'A': 'E'  # Glu
            }
        },
        'U': {
            'G': {
                'G': 'W', # Trytophan (Trp)
                'U': 'C', # Cysteine (Cys)
                'C': 'C', # Cys
                'A': '*'  # Stop
            },
            'U': {
                'G': 'L', # Leucine (Leu)
                'U': 'F', # Phenylalanine (Phe)
                'C': 'F', # Phe
                'A': 'L'  # Leu
            },
            'C': { # Serine (Ser)
                'G': 'S',
                'U': 'S',
                'C': 'S',
                'A': 'S'
            },
            'A': {
                'G': '*', # Stop
                'U': 'Y', # Tyrosine (Tyr)
                'C': 'Y', # Tyr
                'A': '*'  # Stop
            }
        },
        'C': {
            'G': { # Arginine (Arg)
                'G': 'R',
                'U': 'R',
                'C': 'R',
                'A': 'R'
            },
            'U': { # Leucine (Leu)
                'G': 'L',
                'U': 'L',
                'C': 'L',
                'A': 'L'
            },
            'C': { # Proline (Pro)
                'G': 'P',
                'U': 'P',
                'C': 'P',
                'A': 'P'
            },
            'A': { 
                'G': 'Q', # Glutamine (Gln)
                'U': 'H', # histidine (His)
                'C': 'H', # His
                'A': 'Q'  # Gln
            }
        },
        'A': {
            'G': {
                'G': 'R', # Arginine (Arg)
                'U': 'S', # Serine (Ser)
                'C': 'S', # Ser
                'A': 'R'  # Arg 
            },
            'U': {
                'G': 'M', # Methionine (Met)
                'U': 'I', # Isoleucine (Ile)
                'C': 'I', # Ile
                'A': 'I'  # Ile
            },
            'C': { # Threonine (Thr)
                'G': 'T',
                'U': 'T',
                'C': 'T',
                'A': 'T'
            },
            'A': {
                'G': 'K', # Lysine (Lys)
                'U': 'N', # Asparagine (Asn)
                'C': 'N', # Asn
                'A': 'K'  # Lys
            }
        }
    }
    
    def translate(self,k):
        if _debug:
            print('Getting translation for ',k)
        assert(len(k)==3)
        k1 = k[0].upper()
        k2 = k[1].upper()
        k3 = k[2].upper()
        if k1 == 'T':
            k1 = 'U'
        if k2 == 'T':
            k2 = 'U'
        if k3 == 'T':
            k3 = 'U'
        res=None
        level1 = self._store.get(k1,None)
        if level1:
            level2 = level1.get(k2,None)
            if level2:
                res = level2.get(k3,None)
        if _debug and res is None:
            print('\t ie {}{}{}',(k1,k2,k3))
            print('\tFound ',res)
        return res

    def print(self):
        print('===== RNA table =====')
        for k1,v1 in self._store.items():
            for k2,v2 in v1.items():
                for k3,v in v2.items():
                    print('{}{}{} => {}'.format(k1,k2,k3,v))


class RNATranslationTableFlat(RNATranslationTable):
    _store = {
        'UUU':'F',
        'UUC':'F',
        'UUA':'L',
        'UUG':'L',
        'UCU':'S',
        'UCC':'s',
        'UCA':'S',
        'UCG':'S',
        'UAU':'Y',
        'UAC':'Y',
        'UAA':'*',
        'UAG':'*',
        'UGU':'C',
        'UGC':'C',
        'UGA':'*',
        'UGG':'W',
        'CUU':'L',
        'CUC':'L',
        'CUA':'L',
        'CUG':'L',
        'CCU':'P',
        'CCC':'P',
        'CCA':'P',
        'CCG':'P',
        'CAU':'H',
        'CAC':'H',
        'CAA':'Q',
        'CAG':'Q',
        'CGU':'R',
        'CGC':'R',
        'CGA':'R',
        'CGG':'R',
        'AUU':'I',
        'AUC':'I',
        'AUA':'I',
        'AUG':'M',
        'ACU':'T',
        'ACC':'T',
        'ACA':'T',
        'ACG':'T',
        'AAU':'N',
        'AAC':'N',
        'AAA':'K',
        'AAG':'K',
        'AGU':'S',
        'AGC':'S',
        'AGA':'R',
        'AGG':'R',
        'GUU':'V',
        'GUC':'V',
        'GUA':'V',
        'GUG':'V',
        'GCU':'A',
        'GCC':'A',
        'GCA':'A',
        'GCG':'A',
        'GAU':'D',
        'GAC':'D',
        'GAA':'E',
        'GAG':'E',
        'GGU':'G',
        'GGC':'G',
        'GGA':'G',
        'GGG':'G'
    }
    
    def translate(self,k):
        return self._store.get(k,None)

        
