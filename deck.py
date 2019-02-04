# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:51:33 2017

@author: Anthony
"""

def get_deck():
    
    
    u_spade = '\u2660'
    u_heart = '\u2665'
    u_diamond = '\u2666'
    u_club = '\u2663'
    deck = []
    suit = [u_spade, u_heart, u_diamond, u_club]
    s = 0
    
    for i in range(1, 5):
        for x in range(1, 14):
            if x == 11:
                x = "J"
            if x == 12:
                x = "Q"
            if x == 13:
                x = "K"
            if x == 1:
                x = "A"
            else:
                x = str(x)
            deck.append(str(x)+suit[s])
        s += 1
        
    return deck