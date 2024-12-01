def sort_lists(list1, list2):
    list1.sort()
    list2.sort()
    print(f"{list1} {list2}")
    return list1, list2


def list_distances(list1, list2):
    distances = []
    return distances


def total_distance(distances):
    total = 0
    return total


def main():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    assert len(list1) == len(list2), "not the same length!"

    list1, list2 = sort_lists(list1, list2)
    distances = list_distances(list1, list2)
    total = total_distance(distances)

    print(f"Total Distance: {total}")
    return


main()
