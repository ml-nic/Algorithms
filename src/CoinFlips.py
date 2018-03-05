# Counter-Client for simulated coin flip
import random

import math


def flip_coin(T):
    heads_count = 0
    tails_count = 0
    for i in range(T):
        if random.random() < 0.5:
            heads_count += 1
        else:
            tails_count += 1

    print("{} times Head".format(heads_count))
    print("{} times Tails".format(tails_count))
    print("delta: {}".format(math.fabs(heads_count-tails_count)))

if __name__ == "__main__":
    print("How many coin flips?\n")
    flip_coin(int(input()))