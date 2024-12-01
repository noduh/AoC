def sort_lists(list1, list2):
    list1.sort()
    list2.sort()
    return list1, list2


def list_distances(list1, list2):
    assert len(list1) == len(list2), "not the same length!"

    distances = []

    for i in range(len(list1)):
        if list1[i] > list2[i]:
            distances.append(list1[i] - list2[i])
        else:
            distances.append(list2[i] - list1[i])

    return distances


def total_distance(distances):
    total = 0
    for d in distances:
        total += d
    return total

def create_lists(file_location):
    list1 = []
    list2 = []

    return list1, list2

def main():
    list1, list2 = create_lists("challenge_input.txt")

    list1, list2 = sort_lists(list1, list2)
    distances = list_distances(list1, list2)
    total = total_distance(distances)

    print(f"Total Distance: {total}")
    return


main()
