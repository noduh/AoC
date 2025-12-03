INPUT_FILE_LOCATION = "2025/Day 2/input.txt"

def get_ids(file_location: str) -> list[tuple[int, int]]:
    """
    Gets IDs from the given input file
    
    :param file_location: location of the file as a string
    :type file_location: str
    :return: list of ID ranges, where ranges are a tuple containing the IDs in the range
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
