INPUT_FILE_LOCATION = "2025/Day 04/input.txt"


def get_rolls(file_location: str) -> list[list[bool]]:
    """
    Gets the rolls of paper given the input file location

    :param file_location: Location of the input file
    :type file_location: str
    :return: A list of lists representing if there is a roll of paper at a given location
    :rtype: list[list[bool]]
    """
    rolls = []

    with open(file_location, "r") as input_file:
        for line in input_file:
            row = []
            for c in line:
                if c == "@":
                    row.append(True)
                elif c == ".":
                    row.append(False)
            rolls.append(row)
    return rolls


def is_roll_accessible(
    row: int,
    col: int,
    rolls: list[list[bool]],
    radius: int = 1,
    max_surrounding_rolls: int = 3,
) -> bool:
    """
    Determine if a specified roll is accessible

    :param row: the row of the roll to be checked (zero based)
    :type row: int
    :param col: the column of the roll to be checked (zero based)
    :type col: int
    :param rolls: the 2d list of the rolls
    :type rolls: list[list[bool]]
    :param radius: how far out to check
    :type radius: int
    :param max_surrounding_rolls: how many rolls can be around the roll being checked before it becomes inaccessible
    :type max_surrounding_rolls: int
    :return: whether the roll is accessible
    :rtype: bool
    """
    num_rolls_surrounding = 0
    furthest_up = row - radius
    furthest_down = row + radius
    furthest_left = col - radius
    furthest_right = col + radius

    # if adjust the furthest you can check so it doesn't go out of bounds
    if furthest_up < 0:
        furthest_up = 0
    if furthest_down >= len(rolls):
        furthest_down = len(rolls) - 1
    if furthest_left < 0:
        furthest_left = 0
    if furthest_right >= len(rolls[0]):
        furthest_right = len(rolls[0]) - 1

    for row_checking in range(furthest_up, furthest_down + 1):
        for col_checking in range(furthest_left, furthest_right + 1):
            if rolls[row_checking][col_checking] and (row, col) != (
                row_checking,
                col_checking,
            ):
                num_rolls_surrounding += 1

    return num_rolls_surrounding <= max_surrounding_rolls
