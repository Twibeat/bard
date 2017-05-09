# _*_ coding: utf-8 _*_
import itertools

def generate_table():
    chord = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    octave = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    accident = ['', '#', '##', '###', '####', '-', '--', '---', '----', '~', '#~', '`', '-`']
    duration = []
    notes = itertools.product(chord, accident, octave)

    tables = []
    for note in notes:
        tables.append(''.join(note))
    tables.append('rest')#쉼표

    return tables

