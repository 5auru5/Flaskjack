
class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.currency = 100
        self.hand = []
    
    def add_currency(self, amount):
        self.currency += amount
        return self.currency

    def remove_currency(self, amount):
        self.currency -= amount
        return self.currency
    
    def add_card_to_hand(self, card):
        self.hand.append(card)

    def remove_card_to_hand(self, card):
        self.hand.remove(card)

    def clear_hand(self):
        self.hand = {}