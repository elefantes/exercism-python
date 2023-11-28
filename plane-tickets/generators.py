"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_letters = ["A", "B", "C", "D"]
    for i in range(number):
        letter = i % len(seat_letters)
        yield seat_letters[letter]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats_per_row = 4
    row = 1
    for i, col in enumerate(generate_seat_letters(number), 1):
        seat = f"{row}{col}"
        yield seat

        if i % seats_per_row == 0:
            row += 1

        if row == 13:
            row += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = generate_seats(len(passengers))
    result = dict(zip(passengers, seats))

    return result


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    code_length = 12
    for seat in seat_numbers:
        code_prefix = f"{seat}{flight_id}"
        padding_length = code_length - len(code_prefix)
        padding = "0" * padding_length
        code = f"{code_prefix}{padding}"
        yield code
