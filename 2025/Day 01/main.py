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


def main():
    current_location = 50
    password = 0
    steps = get_steps("2025/Day 01/input.txt")
    for step in steps:
        current_location = (current_location + step[0] * step[1]) % 100
        if current_location == 0:
            password += 1
    print(password)


main()
