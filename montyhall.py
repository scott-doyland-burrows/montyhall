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

    # Randomly switch or stay
    switched = random.choice([True, False])
    final_door = other_door if switched else chosen_door

    # Check if won
    won = (final_door == prize_door)

    if won:
        if switched:
            wins_switched += 1
        else:
            wins_stayed += 1

print(f"\nResults after {num_games} games:")
print(f"Wins when switched: {wins_switched}")
print(f"Wins when stayed: {wins_stayed}")
print(f"Total wins: {wins_switched + wins_stayed}")
print(f"Win rate when switched: {wins_switched / (num_games / 2):.1%}")
print(f"Win rate when stayed: {wins_stayed / (num_games / 2):.1%}")
