import random


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def main():
    player1 = input("Player 1's name:\n")
    player2 = input("Player 2's name:\n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)


main()
