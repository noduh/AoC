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
