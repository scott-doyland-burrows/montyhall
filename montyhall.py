"""Monty Hall problem simulator."""
import sys
from multiprocessing import Pool, cpu_count

import numpy as np


BATCH_SIZE = 10_000_000


def run_batch(args):
    """Run a batch of games and return wins_stayed count."""
    batch_size, doors = args
    prize_doors = np.random.randint(0, doors, batch_size)
    chosen_doors = np.random.randint(0, doors, batch_size)
    return np.sum(chosen_doors == prize_doors)


num_games = int(input("Number of games: "))
num_doors = int(input("Number of doors: "))

if num_doors < 2:
    print("Must enter 2 or more doors")
    sys.exit()

# Create batch arguments
batches = []
for start in range(0, num_games, BATCH_SIZE):
    current_batch = min(BATCH_SIZE, num_games - start)
    batches.append((current_batch, num_doors))

# Process batches in parallel
with Pool(cpu_count()) as pool:
    results = pool.map(run_batch, batches)

wins_stayed = sum(results)

wins_switched = num_games - wins_stayed

print(f"\nResults after {num_games} games:")
print(f"Wins when switched: {wins_switched} ({wins_switched / num_games:.10%})")
print(f"Wins when stayed: {wins_stayed} ({wins_stayed / num_games:.10%})")
