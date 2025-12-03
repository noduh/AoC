INPUT_FILE_LOCATION = "2025/Day 2/input.txt"


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
    id_string = str(id)
    id_string_length = len(id_string)
    if id_string_length % 2 != 0:  # if the id is an odd length, it must be valid
        return True
    if id_string[(id_string_length // 2) :] == id_string[: (id_string_length // 2)]:
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


main()
