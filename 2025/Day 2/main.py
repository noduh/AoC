INPUT_FILE_LOCATION = "2025/Day 2/input.txt"


def split_string(string_to_split: str, substring_length: int) -> list[str]:
    """
    Splits the string into even parts and returns a list

    :param string_to_split: the original string to split it into
    :type string_to_split: str
    :param substring_length: the preferred length of each substring
    :type substring_length: int
    :return: a list of substrings taken from the original string
    :rtype: list[str]
    """
    substrings = []
    while len(string_to_split) >= substring_length:
        substring = string_to_split[:substring_length]
        substrings.append(substring)
        string_to_split = string_to_split[substring_length:]
    substrings.append(string_to_split)
    return substrings


def get_id_ranges(file_location: str) -> list[tuple[int, int]]:
    """
    Gets IDs from the given input file

    :param file_location: location of the file as a string
    :type file_location: str
    :return: list of ID ranges, where ranges are a tuple containing the IDs on each end of the range
    :rtype: list[tuple[int, int]]
    """
    file_string = ""
    id_list = []
    with open(file_location, "r") as file:
        file_string = file.read()
    id_range_list = file_string.split(",")
    for id_range in id_range_list:
        id_range_list = id_range.split("-")
        id_list.append((int(id_range_list[0]), int(id_range_list[1])))
    return id_list


def check_id_validity(id: int) -> bool:
    """
    Checks the validity of the id

    :param id: the id to check
    :type id: int
    :return: returns a boolean that says if it's a valid id
    :rtype: bool
    """
    id_string = str(id)
    id_string_length = len(id_string)
    for i in range(1, id_string_length // 2):
        if id_string_length % i != 0:  # if the id is not divisible, it must be valid
            return True
        id_string_substrings = split_string(id_string, i)
        for substring in id_string_substrings:
            if substring != id_string_substrings[0]:
                return False
    return True


def main():
    id_ranges = get_id_ranges(INPUT_FILE_LOCATION)
    invalid_ids = []
    sum_invalid_ids = 0
    for id_range in id_ranges:
        start_id = id_range[0]
        end_id = id_range[1]
        current_id = start_id
        while current_id <= end_id:
            if check_id_validity(current_id) == False:
                invalid_ids.append(current_id)
            current_id += 1
    for id in invalid_ids:
        sum_invalid_ids += id
    print(sum_invalid_ids)


# main()
print(check_id_validity(123123123)) # false
print(check_id_validity(1231231234)) # true
print(check_id_validity(1212121212)) # false
print(check_id_validity(12345678)) # true