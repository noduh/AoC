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


def total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def create_lists(file_location):
    list1 = []
    list2 = []

    with open(file_location, "r") as file:
        for line in file:
            line.strip()
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))

    return list1, list2


def main():
    list1, list2 = create_lists("Dec 01/challenge_input.txt")

    list1, list2 = sort_lists(list1, list2)
    distances = list_distances(list1, list2)
    total = total(distances)

    print(f"Total Distance: {total}")
    return


main()
