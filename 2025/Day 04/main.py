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
