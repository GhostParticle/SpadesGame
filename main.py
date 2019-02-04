# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:31:05 2017

@author: ghostpartical
"""


#import deck
import random
#import select_card
import base_Functions
import testFile

p1 = []
p2 = []
p3 = []
p4 = []
players = [p1, p2, p3, p4]


def main():
    
    new_deck = base_Functions.get_deck()
    random.shuffle(new_deck)
    base_Functions.get_cards(new_deck, players, p1, p2, p3, p4)
    base_Functions.card_count(players, p1, p2, p3, p4)
    testFile.card_orginize(players, p1)
    print("Here are your cards:  {}".format(players[0]))
        
main()

