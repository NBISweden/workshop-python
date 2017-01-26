#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# http://www2.sluh.org/bioweb/bi100/tutorials/thegeneticcode/codonwheel2.jpg
# https://en.wikipedia.org/wiki/Protein_primary_structure

from pprint import pprint

class RNATranslationTableBase():
    _store = None
    def print(self):
        pprint(self._store)
    def translate(self,key):
        pass

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
    
    # @print_args
    # @print_retval
    def translate(self,codon):
        assert(len(codon)==3)
        k = codon.upper().replace('T','U')
        k1,k2,k3 = k[0], k[1], k[2]
        if k1 == 'N' or k2 == 'N' or k3 == 'N':
            raise ValueError('Eh... N??')

        level1 = self._store.get(k1,None)
        if level1:
            level2 = level1.get(k2,None)
            if level2:
                return level2.get(k3,None)
        return none

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

    def print(self):
        print('===== RNA table =====')
        for codon,value in self._store.items():
            print(codon,' => ',value)

        
