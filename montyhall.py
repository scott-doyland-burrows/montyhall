"""Monyt Hall"""
import random

num_games = int(input("Number of games: "))
num_doors = int(input("Number of doors: "))

wins_switched = 0
wins_stayed = 0

for game in range(num_games):
    # Place prize and make initial choice
    prize_door = random.randint(0, num_doors - 1)
    chosen_door = random.randint(0, num_doors - 1)

    # Determine the other remaining door
    if chosen_door == prize_door:
        # Player chose prize, keep a random other door
        other_door = random.choice([d for d in range(num_doors) if d != chosen_door])
    else:
        # Keep the prize door
        other_door = prize_door

    # Test both strategies
    if chosen_door == prize_door:
        wins_stayed += 1
    else:
        wins_switched += 1

print(f"\nResults after {num_games} games:")
print(f"Wins when switched: {wins_switched} ({wins_switched / num_games:.3f})")
print(f"Wins when stayed: {wins_stayed} ({wins_stayed / num_games:.3f})")
