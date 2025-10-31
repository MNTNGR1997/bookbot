from stats import get_word_count, get_character_count, sort_character_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_name = sys.argv[1]

def get_book_text(book_name):
    with open(book_name, "r") as file:
        return file.read()

def main():
    book_text = get_book_text(book_name)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = sort_character_count(character_count)
    print(f"Found {word_count} total words.")
    for item in sorted_character_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()