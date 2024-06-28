
# Consider the following game: you start with two decks of n playing
# cards each (shuffled). At each round, you remove one or two cards as
# follows. If the two cards at the top of the two decks have the same
# suit or the same numeric value, you may remove both of them at no
# cost. If the two cards have different suits and numbers, or if you
# do not choose to remove both of them, you must choose to remove one
# of the two cards at a cost corresponding to its numeric value. If one
# of the decks is empty, you have no choice: you must remove the card
# on the remaining deck at the cost of its numeric value. The game ends
# when both decks are empty. Now consider the following decision problem:
# given the two initial shuffled decks A and B and a maximal cost c,
# decide whether it is possible to play a game with a total cost less
# than c. A and B are arrays of cards; the functions suit(x) and value(x)
# return, in O(1) time, the suit and numeric value of a card x, respectively.
# For example, suit(A[i]) returns the suit of the the i-th card on the A deck.
# Ace value is 11, figures value is 10, the rest of the card have number == value
# Write a solution algorithm
# Write a resolution algorithm

from enum import Enum


class Suit(Enum):
    DIAMOND = 1
    CLUB = 2
    HEART = 3
    SPADE = 4


class Face(Enum):
    ACE = 1
    KING = 2
    QUEEN = 3
    JACK = 4


class Card():
    def __init__(self, number: int or Face, suit: Suit):
        if type(number) != Face:
            if number > 10 or number < 2:
                number = 2

        if not isinstance(suit, Suit):
            suit = Suit.SPADE

        self.number = number
        self.suit = suit

    def get_value(self) -> int:
        if not isinstance(self.number, Face):
            return self.number

        if self.number == Face.ACE:
            return 11

        return 10

    def get_suit(self) -> Suit:
        return self.suit


def card_game_solution(A: list[Card], B: list[Card], cost: int, S: bool):
    return card_game_resolution(A, B, cost) == S


def card_game_resolution(A: list[Card], B: list[Card], cost: int):
    cache = [[None] * (len(A) + 1) for i in range(len(B) + 1)]

    # Starts from cost 0
    cache[len(B)][len(A)] = 0

    # Fill bottom row
    for i in range(len(A) - 1, -1, -1):
        cache[len(B)][i] = A[i].get_value() + cache[len(B)][i + 1]

    # Fill right column
    for j in range(len(B) - 1, -1, -1):
        cache[j][len(A)] = B[j].get_value() + cache[j + 1][len(A)]

    # Calculate
    for r in range(len(B) - 1, -1, -1):
        for c in range(len(A) - 1, -1, -1):
            if A[c].get_value() == B[r].get_value() or A[c].get_suit() == B[r].get_suit():
                cache[r][c] = cache[r + 1][c + 1]
            else:
                cache[r][c] = min(cache[r][c + 1] +
                                  A[c].get_value(), cache[r + 1][c] + B[r].get_value())

    print()
    for r in range(len(cache)):
        for c in range(len(cache[r])):
            if len(str(cache[r][c])) == 1:
                print(f" {cache[r][c]} ", end="")
                continue

            print(f"{cache[r][c]} ", end="")
        print()
    print()

    return cache[0][0] < cost


if __name__ == "__main__":

    A = [
        Card(Face.KING, Suit.SPADE),
        Card(6, Suit.SPADE),
        Card(5, Suit.DIAMOND),
        Card(4, Suit.CLUB),
        Card(2, Suit.SPADE),
        Card(8, Suit.SPADE),
    ]
    B = [
        Card(Face.QUEEN, Suit.HEART),
        Card(6, Suit.CLUB),
        Card(Face.JACK, Suit.DIAMOND),
        Card(Face.ACE, Suit.DIAMOND),
        Card(8, Suit.SPADE),
    ]

    print(card_game_resolution(A, B, 20))
    print(card_game_solution(A, B, 20, True))
