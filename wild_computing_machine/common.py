import random


def roll_ndn(dice: list) -> list:
    rolls = []
    for _ in range(dice[0]):
        rolls.append(random.randint(1, dice[1]))
    return rolls


def plural(in_: str) -> str:
    return in_ + 's' if in_ != 'wolf' else 'wolves'
