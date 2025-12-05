INPUT_FILE_LOCATION = "2025/Day 03/input.txt"


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
            banks_string.append(line)
    for bank_string in banks_string:
        bank_length = len(bank_string)
        bank_num = int(bank_string)
        bank = []
        for i in range(2, bank_length + 1):
            bank.append(bank_num // (10 ** (bank_length - i)))
            bank_num %= 10 ** (bank_length - i)
        banks.append(bank)
    return banks


def find_largest_joltage(bank: list[int]) -> int:
    first_battery_joltage = 0
    second_battery_joltage = 0
    total_joltage = 0
    second_battery_start_index = 0
    for i in range(len(bank) - 2):  # only go to the second-to-last index
        if bank[i] > first_battery_joltage:
            first_battery_joltage = bank[i]
            second_battery_start_index = i + 1
    for i in range(second_battery_start_index, len(bank) - 1):
        if bank[i] > second_battery_joltage:
            second_battery_joltage = bank[i]
    total_joltage = int(str(first_battery_joltage) + str(second_battery_joltage))
    return total_joltage


def main():
    pass


main()
