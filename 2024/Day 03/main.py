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
    return True, None


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
