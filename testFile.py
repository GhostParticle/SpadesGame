# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:17:52 2017

@author: ghostpartical
"""

u_spade = '\u2660'
u_heart = '\u2665'
u_diamond = '\u2666'
u_club = '\u2663'
suit = [u_spade, u_heart, u_diamond, u_club]
clubs = []
diamond = []
hearts = []
spades = []
player_cards = [clubs, diamond, hearts, spades]


def card_splitter_2(a, b):
    if b[1] == u_club:
        clubs.append(a)
    elif b[1] == u_diamond:
        diamond.append(a)
    elif b[1] == u_heart:
        hearts.append(a)
    elif b[1] == u_spade:
        spades.append(a)
        
def card_splitter_3(a, b):
    if b[2] == u_club:
        clubs.append(a)
    elif b[2] == u_diamond:
        diamond.append(a)
    elif b[2] == u_heart:
        hearts.append(a)
    elif b[2] == u_spade:
        spades.append(a)
        
def card_placement(player_cards):
    z = 0
    while z < len(player_cards):
        suit_hand = player_cards[z]
        print(suit_hand)
        j = 0 
        while j < len(suit_hand):
            a = suit_hand[j]
            if len(a) >2:
                b = int(a[0] + a[1])
                print(b)
            else:
                
                if b == "K":
                    b = 13
                    print(b)
                if b == "Q":
                    b == 12
                    print(b)
                if b == "J":
                    b == 11
                    print(b)
                else:
                    b = a[0]
                    print(b)
            j += 1
        #print(lowest)
        
        z += 1

def card_orginize(players, p1):
    
    x = 0
    while x < len(p1):
        a = p1[x]
        if len(a) < 3:
            b = [a[0], a[1]]
            card_splitter_2(a,b)
        elif len(a) == 3:
            b = [a[0], a[1], a[2]]
            card_splitter_3(a,b)
        x += 1
        
    
    print(clubs, diamond, hearts, spades)
    card_placement(player_cards)

    
    