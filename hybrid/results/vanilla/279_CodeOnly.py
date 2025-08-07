import random
from collections import Counter

# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def task_func(x=1):
    # Initialize a list to store the hands
    hands = []
    # Initialize a list to store all drawn cards
    drawn_cards = []

    # Draw x hands
    for _ in range(x):
        # Randomly select 5 cards without replacement
        hand = random.sample(CARDS, 5)
        # Add the hand to the list of hands
        hands.append(hand)
        # Add the cards in the hand to the drawn cards list
        drawn_cards.extend(hand)

    # Create a counter for the drawn cards
    card_counter = Counter(drawn_cards)

    # Return the list of hands and the counter
    return hands, card_counter

# Example usage:
# hands, counter = task_func(3)
# print("Hands:", hands)
# print("Counter:", counter)