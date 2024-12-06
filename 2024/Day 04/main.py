def get_challenge_input(file_path: str) -> list[str]:
    """Takes the challenge input and puts each line in the file into an element in the returned list"""
    challenge_input = []
    with open(file_path, "r") as file:
        challenge_input = file.readlines()

    return challenge_input


def search_letter(
    line: int, string_location: int, word_to_search: str, challenge_input: list[str]
) -> int:
    """Takes the location of the letter to search, and checks each direction in the input. It returns the number of times the letter leads to a full result of the searched word"""
    return 0


def search_input(word_to_search: str, challenge_input: list[str]) -> int:
    """Takes the challenge input and searches it to find the number of occurrences of the specified word. Returns that count."""
    return 0


def main():
    challenge_input = get_challenge_input("2024\Day 04\challenge_input.txt")
    word_to_search = "XMAS"
    count = search_input(word_to_search, challenge_input)
    print(f"Found the word {word_to_search} {count} times!")


main()
