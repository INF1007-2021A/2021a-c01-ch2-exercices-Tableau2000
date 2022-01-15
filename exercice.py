#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    for lettre in mot:
        if 97 <= lettre <= 122:
            mot += chr(ord(lettre) - 32)
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
