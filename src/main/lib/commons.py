###################################
#First commit by Gunnar Ohlson
# This is placeholder text for now
# Common functions and methods will 
# Live here
###################################
from lib.deck import Deck
from lib.player import Player


def hit(current_deck : Deck, current_player : Player):
    return current_player.add_card_to_hand(current_deck.draw())

def stay():
    pass

def split():
    pass

def bet(current_player : Player, amount : int):
    return current_player.remove_currency(amount)
2
