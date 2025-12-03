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

def main():
    current_location = 50
    password = 0
    steps = get_steps("2025/Day 01/test_input.txt")
    for step in steps:
        previous_sign = get_sign(current_location)
        distance = step[1]
        direction = step[0]
        password += distance // 100 # accounts for distances greater than 100
        distance = distance % 100   # 󱟀
        current_location = (current_location + direction * distance) # gets new location
        if current_location != current_location % 100 and current_location % 100 != 0: # checks if simplifying indicates passing 0
            password += 1
            current_location = current_location % 100 # simplifies
        elif current_location != 0 and get_sign(current_location) != previous_sign: # checks if the sign has fully changed
            password += 1
        elif current_location == 0:
            password += 1
    print(password)


main()
