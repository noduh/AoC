def get_input(file_location: str) -> str:
    """takes the file and turns it into a string"""
    file_input = ""
    with open(file_location, "r") as file:
        file_input = file.read()
    return file_input


def get_command_inputs(command: str, input_string: str) -> list[str]:
    """returns the inputs for each time the specified command is found"""
    inputs = []
    return inputs


def get_multiply_data(command_input: str) -> tuple[bool, tuple[int, int]]:
    """checks if the input is valid for the multiply command"""
    x = None
    y = None
    can_multiply = True
    input_string = command_input # will no longer remove parentheses. this will happen before the function is called
    input_data = []

    # check for invalid whitespace
    if input_string == input_string.strip():
        input_string = input_string.replace(" ", ".") # helps casting fail invalid inputs with extra whitespace
        input_data = input_string.split(",")
    else:
        can_multiply = False

    if not can_multiply and len(input_data) != 2:
        can_multiply = False
    else:
        try:
            x = int(input_data[0])
            y = int(input_data[1])
        except ValueError:
            can_multiply = False

    return can_multiply, (x, y)


def multiply(x: int, y: int) -> int:
    """multiplies the two specified numbers and returns the product"""
    return x * y


def total(numbers: list[int]) -> int:
    """Totals all the numbers in a list"""
    total = 0
    for n in numbers:
        total += n
    return total


def main():
    products = []
    input_string = get_input("2024\Day 03\challenge_input.txt")
    command_inputs = get_command_inputs("mul", input_string)
    for command_input in command_inputs:
        can_multiply, data = get_multiply_data(command_input)
        if can_multiply:
            x, y = data
            products.append(multiply(x, y))

    product_total = total(products)

    print(f"Total of Products: {product_total}")


main()


# # TESTING
# can_multiply, (x, y) = get_multiply_data("10, 15")
# print(f"{can_multiply} | {x}*{y}")

# can_multiply, (x, y) = get_multiply_data("10,15")
# print(f"{can_multiply} | {x}*{y}")

# can_multiply, (x, y) = get_multiply_data(" 10,15")
# print(f"{can_multiply} | {x}*{y}")

# can_multiply, (x, y) = get_multiply_data("a10,15")
# print(f"{can_multiply} | {x}*{y}")