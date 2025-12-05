INPUT_FILE_LOCATION = "2025/Day 03/input.txt"
NUMBER_OF_BATTERIES_PER_BANK = 12


def get_battery_banks(file_location: str) -> list[list[int]]:
    """
    Turns the input file into a useful list of battery banks

    :param file_location: location of the input file
    :type file_location: str
    :return: list of banks which are lists of batteries
    :rtype: list[list[int]]
    """
    banks_string = []
    banks = []
    with open(file_location, "r") as file:
        for line in file:
            banks_string.append(line.replace("\n", ""))
    for bank_string in banks_string:
        bank_length = len(bank_string)
        bank_num = int(bank_string)
        bank = []
        for i in range(1, bank_length + 1):
            bank.append(bank_num // (10 ** (bank_length - (i))))
            bank_num %= 10 ** (bank_length - (i))
        banks.append(bank)
    return banks


def find_largest_joltage(
    bank: list[int], max_size: int, starting_index: int = 0
) -> str:
    """
    Finds the largest joltage in the given bank

    :param bank: the bank containing the batteries
    :type bank: list[int]
    :param max_size: the amount of batteries to be turned on in the bank
    :type max_size: int
    :param starting_index: index to start searching the bank from
    :type starting_index: int
    :return: the largest possible output joltage of the bank
    :rtype: int
    """
    if max_size == 0:  # end of the recursion
        return ""

    total_joltage = 0
    max_battery_joltage = 0
    new_starting_index = 0
    for i in range(starting_index, len(bank) - (max_size - 1)):
        if bank[i] > max_battery_joltage:
            max_battery_joltage = bank[i]
            new_starting_index = i + 1
    total_joltage = int(
        str(total_joltage)
        + str(max_battery_joltage)
        + str(find_largest_joltage(bank, max_size - 1, new_starting_index))
    )
    return str(total_joltage)

    # first_battery_joltage = 0
    # second_battery_joltage = 0
    # total_joltage = 0
    # second_battery_start_index = 0
    # for i in range(len(bank) - 1):  # only go to the second-to-last index
    #     if bank[i] > first_battery_joltage:
    #         first_battery_joltage = bank[i]
    #         second_battery_start_index = i + 1
    # for i in range(second_battery_start_index, len(bank)):
    #     if bank[i] > second_battery_joltage:
    #         second_battery_joltage = bank[i]
    # total_joltage = int(str(first_battery_joltage) + str(second_battery_joltage))
    # return total_joltage


def main():
    battery_banks = get_battery_banks(INPUT_FILE_LOCATION)
    total_output_joltage = 0
    for bank in battery_banks:
        total_output_joltage = total_output_joltage + int(
            find_largest_joltage(bank, NUMBER_OF_BATTERIES_PER_BANK)
        )
    print(total_output_joltage)


main()
