#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for translatingDNA into proteins.
Read more here:
 http://www2.sluh.org/bioweb/bi100/tutorials/thegeneticcode/codonwheel2.jpg
 https://en.wikipedia.org/wiki/Protein_primary_structure
"""


def translate_dna(dna):
    """ Translate a DNA sequence into proteins """
    amino_seq = []
    # split into codons
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        amino = translate(codon)
        if amino == '*':  # stop signal
            break
        amino_seq.append(amino)
    return ''.join(amino_seq)


def translate(codon):
    """ Translate a codon to an amino acid """
    assert len(codon) == 3
    # Translate DNA -> RNA
    rna_codon = codon.upper().replace('T', 'U')
    k1, k2, k3 = rna_codon[0], rna_codon[1], rna_codon[2]

    if 'N' in rna_codon:
        # Cannot translate unkonwn bases
        raise ValueError(f'Unknown base N in {rna_codon}')

    level1 = _TRANSLATION_STORE.get(k1, None)
    if level1:
        level2 = level1.get(k2, None)
        if level2:
            return level2.get(k3, None)
    return None


def print_table():
    """ Print the full translation table """
    print('===== RNA table =====')
    for k1, v1 in _TRANSLATION_STORE.items():
        for k2, v2 in v1.items():
            for k3, v in v2.items():
                print(f'{k1}{k2}{k3} => {v}')


# Combinations of RNA bases and the resulting amino acid
_TRANSLATION_STORE = {
    'G': {
        'G': {  # Glycine (Gly)
            'G': 'G',
            'U': 'G',
            'C': 'G',
            'A': 'G'
        },
        'U': {  # Valine (Val)
            'G': 'V',
            'U': 'V',
            'C': 'V',
            'A': 'V'
        },
        'C': {  # Alanine (Ala)
            'G': 'A',
            'U': 'A',
            'C': 'A',
            'A': 'A'
        },
        'A': {
            'G': 'E',  # Glutamic acid (Glu)
            'U': 'D',  # Aspartic acid (Asp)
            'C': 'D',  # Asp
            'A': 'E'  # Glu
        }
    },
    'U': {
        'G': {
            'G': 'W',  # Trytophan (Trp)
            'U': 'C',  # Cysteine (Cys)
            'C': 'C',  # Cys
            'A': '*'  # Stop
        },
        'U': {
            'G': 'L',  # Leucine (Leu)
            'U': 'F',  # Phenylalanine (Phe)
            'C': 'F',  # Phe
            'A': 'L'  # Leu
        },
        'C': {  # Serine (Ser)
            'G': 'S',
            'U': 'S',
            'C': 'S',
            'A': 'S'
        },
        'A': {
            'G': '*',  # Stop
            'U': 'Y',  # Tyrosine (Tyr)
            'C': 'Y',  # Tyr
            'A': '*'  # Stop
        }
    },
    'C': {
        'G': {  # Arginine (Arg)
            'G': 'R',
            'U': 'R',
            'C': 'R',
            'A': 'R'
        },
        'U': {  # Leucine (Leu)
            'G': 'L',
            'U': 'L',
            'C': 'L',
            'A': 'L'
        },
        'C': {  # Proline (Pro)
            'G': 'P',
            'U': 'P',
            'C': 'P',
            'A': 'P'
        },
        'A': {
            'G': 'Q',  # Glutamine (Gln)
            'U': 'H',  # histidine (His)
            'C': 'H',  # His
            'A': 'Q'  # Gln
        }
    },
    'A': {
        'G': {
            'G': 'R',  # Arginine (Arg)
            'U': 'S',  # Serine (Ser)
            'C': 'S',  # Ser
            'A': 'R'  # Arg
        },
        'U': {
            'G': 'M',  # Methionine (Met)
            'U': 'I',  # Isoleucine (Ile)
            'C': 'I',  # Ile
            'A': 'I'  # Ile
        },
        'C': {  # Threonine (Thr)
            'G': 'T',
            'U': 'T',
            'C': 'T',
            'A': 'T'
        },
        'A': {
            'G': 'K',  # Lysine (Lys)
            'U': 'N',  # Asparagine (Asn)
            'C': 'N',  # Asn
            'A': 'K'  # Lys
        }
    }
}
