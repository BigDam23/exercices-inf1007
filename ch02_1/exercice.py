#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    mot2 = ''
    for i in mot:
        mot2 += chr(ord(i) - 32)
    mot = mot2
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
