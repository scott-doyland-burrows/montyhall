"""Monty Hall problem simulator."""
import sys
import numpy as np

BATCH_SIZE = 10_000_000

num_games = int(input("Number of games: "))
num_doors = int(input("Number of doors: "))

if num_doors < 2:
    print("Must enter 2 or more doors")
    sys.exit()

# Process in batches to avoid memory issues
wins_stayed = 0
wins_switched = 0

for start in range(0, num_games, BATCH_SIZE):
    current_batch = min(BATCH_SIZE, num_games - start)
    prize_doors = np.random.randint(0, num_doors, current_batch)
    chosen_doors = np.random.randint(0, num_doors, current_batch)
    wins_stayed += np.sum(chosen_doors == prize_doors)

wins_switched = num_games - wins_stayed

print(f"\nResults after {num_games} games:")
print(f"Wins when switched: {wins_switched} ({wins_switched / num_games:.10%})")
print(f"Wins when stayed: {wins_stayed} ({wins_stayed / num_games:.10%})")
