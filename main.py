import sys
from stats import count_characters, count_words, sort_characters

if sys.argv < 2:
    print("Usage: python main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[2]

word_count = count_words(book_path) 
character_count = count_characters(book_path)
character_sort = sort_characters(character_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for entry in character_sort:
    print(f"{entry["char"]}: {entry["num"]}")
print("============= END ===============")


