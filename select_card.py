# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:31:37 2017

@author: ghostpartical
"""



def get_cards(new_deck, players, p1, p2, p3, p4):
    

    while len(new_deck) > 0:
        card = new_deck.pop()
        p1.append(card)
        card = new_deck.pop()
        p2.append(card)
        card = new_deck.pop()
        p3.append(card)
        card = new_deck.pop()
        p4.append(card)
   
    return players
    




