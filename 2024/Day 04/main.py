def get_challenge_input(file_path: str) -> list[str]:
    """Takes the challenge input and puts each line in the file into an element in the returned list"""
    challenge_input = []
    with open(file_path, "r") as file:
        challenge_input = file.readlines()

    return challenge_input


def search_letter(
    line_start: int, char_start: int, word_to_search: str, challenge_input: list[str]
) -> int:
    """Takes the location of the letter to search, and checks each direction in the input. It returns the number of times the letter leads to a full result of the searched word"""
    NORTH = 0, 1
    NORTHEAST = 1, 1
    EAST = 1, 0
    SOUTHEAST = 1, -1
    SOUTH = 0, -1
    SOUTHWEST = -1, -1
    WEST = -1, 0
    NORTHWEST = -1, 1
    directions = [NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST]

    # Automatically return 0 if it doesn't work in any direction
    if challenge_input[line_start][char_start] != word_to_search[0]:
        return 0

    for multiplier, letter in enumerate(
        word_to_search, 1
    ):  # multiplier lets us find the specific line and character easily
        for direction in directions:
            line_direction, char_direction = direction
            line_index = line_direction * multiplier + line_start
            char_num = char_direction * multiplier + char_start
            if 0 > line_index > len(challenge_input) or 0 > char_num > len(
                challenge_input[line_index]
            ):
                directions.remove(direction)
            elif challenge_input[line_index][char_num] != letter:
                directions.remove(direction)

    return len(directions)


def search_input(word_to_search: str, challenge_input: list[str]) -> int:
    """Takes the challenge input and searches it to find the number of occurrences of the specified word. Returns that count."""
    total_found = 0

    for line_number, line in enumerate(challenge_input):
        for char_number, char in enumerate(line):
            if char == word_to_search[0]:
                total_found += search_letter(
                    line_number, char_number, word_to_search, challenge_input
                )

    return total_found


def main():
    challenge_input = get_challenge_input("2024\Day 04\challenge_input.txt")
    word_to_search = "XMAS"
    count = search_input(word_to_search, challenge_input)
    print(f"Found the word {word_to_search} {count} times!")


main()

# # tests
# print(
#     search_letter(0, 4, "XMAS", get_challenge_input("2024\Day 04\challenge_input.txt"))
# )
