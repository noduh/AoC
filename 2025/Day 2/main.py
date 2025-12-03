def get_ids(file_location: str) -> list[tuple[int, int]]:
    file_string = ""
    id_list = []
    with open(file_location, "r") as file:
        file_string = file.read()
    id_range_list = file_string.split(",")
    for id_range in id_range_list:
        id_range_list = id_range.split("-")
        id_list.append((int(id_range_list[0]), int(id_range_list[1])))
    return id_list
