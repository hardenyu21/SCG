from collections import Counter
import random

# Constants
HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']

def task_func():
    # Generate a list of five cards
    hand = [random.choice(HAND_RANKS) + random.choice(SUITS) for _ in range(5)]
    
    # Extract the ranks from the hand
    ranks = [card[:-1] for card in hand]
    
    # Count the frequency of each card rank
    rank_count = Counter(ranks)
    
    return hand, rank_count

# Example usage
hand, rank_count = task_func()
print("Hand:", hand)
print("Rank Count:", rank_count)