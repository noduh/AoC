def get_steps(file_location: str) -> list[tuple[int, int]]:
    """
    Returns the steps to take for the combination given the challenge input file.

    :param file_location: The file location of the challenge input.
    :type file_location: str
    :return: List of steps, the first number in the tuple being a direction (1 or -1) and the second being the number of clicks in the rotation.
    :rtype: list[tuple[int, int]]
    """
    steps = []
    with open(file_location, "r") as file:
        step = None, None
        for line in file:
            direction_str = line[0]
            direction = None
            if direction_str == "R":
                direction = 1
            elif direction_str == "L":
                direction = -1
            line = line.replace(direction_str, "")
            step = direction, int(line)
            steps.append(step)

    return steps


def get_sign(number: int | float) -> int:
    """
    Docstring for get_sign

    :param number: any real number
    :type number: int | float
    :return: either 1 or -1 to indicate positive or negative, or 0 to indicate neither
    :rtype: int
    """
    if number == 0:
        return 0
    return int(number / abs(number))


def simplify_location(number: int) -> int:
    """
    Docstring for simplify_location

    :param number: location as a raw number
    :type number: int
    :return: the actual location after simplifying the number
    :rtype: int
    """
    number %= 100
    if get_sign(number) == -1:
        number += 100
    return number


def main():
    current_location = 50
    password = 0
    steps = get_steps("2025/Day 01/input.txt")
    for step in steps:
        distance = step[1]
        direction = step[0]
        for _ in range(distance):
            current_location += direction
            current_location = simplify_location(current_location)
            if current_location == 0:
                password += 1
    print(password)


main()
