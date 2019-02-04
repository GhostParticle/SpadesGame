# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:49:13 2017

@author: Anthony
"""
# Gets each players card count
def card_count(players, p1, p2, p3, p4):
    x = 0
    while x <= 3:
        print("Player {} Card Count = {}".format(x + 1, len(players[x])))
        x +=1
    
#Gets a new deck of cards
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

# Passes the cards out to players from the new deck
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