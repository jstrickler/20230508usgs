from itertools import product

ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
suits = "Clubs Diamonds Hearts Spades".split()

card_deck = product(ranks, suits)
print(f"card_deck: {list(card_deck)}")
