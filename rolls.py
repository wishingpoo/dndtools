from random import randint


def roll(n):
    return randint(1, n)


def percentile():
    return roll(100)


def d4():
    return roll(4)


def d6():
    return roll(6)


def d8():
    return roll(8)


def d10():
    return roll(10)


def d12():
    return roll(12)


def d20():
    return roll(20)


def rep(f, n):
    return sum((f() for _ in range(n)))
