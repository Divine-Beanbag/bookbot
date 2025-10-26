from stats import count_characters, count_words 

book_path = "books/frankenstein.txt" #you have to make file paths a string

word_count = count_words(book_path) 

character_count = count_characters(book_path)

print(f"Found {word_count} total words")
print(character_count)


