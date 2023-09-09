"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in ['Q', 'K', 'J']:
        value = 10
    elif card == 'A':
        value = 1
    else:
        value = int(card)

    return value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """


    if value_of_card(card_one) == value_of_card(card_two):
        result = (card_one, card_two)
    elif value_of_card(card_one) > value_of_card(card_two):
        result = card_one
    else:
        result = card_two

    return result


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    blackjack = 21
    high = 11
    low = 1
    
    sum_cards = value_of_card(card_one) + value_of_card(card_two)
    
    if card_one == 'A':
        sum_cards += 10
    if card_two == 'A':
        sum_cards += 10

    if blackjack - sum_cards >= high: 
        result = high
    else:
        result = low

    return result


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    
    sum_cards = value_of_card(card_one) + value_of_card(card_two)
    
    if card_one == 'A':
        sum_cards += 10
    if card_two == 'A':
        sum_cards += 10

    return sum_cards == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    sum_cards = value_of_card(card_one) + value_of_card(card_two)

    if sum_cards not in range(9,12) and card_one == 'A':
        sum_cards += 10

    if sum_cards not in range(9,12) and card_two == 'A':
        sum_cards += 10

    
    return sum_cards in range(9,12)
