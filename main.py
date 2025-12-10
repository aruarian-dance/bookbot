import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    print(get_book_text(sys.argv[1]))

from stats import word_count
from stats import character_count
from stats import sort_characters

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

counts = character_count(get_book_text(sys.argv[1]))
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
word_count(get_book_text(sys.argv[1]))
print("--------- Character Count -------")
for item in sort_characters(counts):
    print(f"{item["char"]}: {item["num"]}")
print("============= END ===============")
