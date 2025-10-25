book_path = "books/frankenstein.txt" #you have to make file paths a string

def get_book_text(book_path): #this function puts all the book contents into a variable
    with open(book_path) as f: #opens the book file as a file object
        file_contents = f.read() #stores the contents of the file as
        num_words = len(file_contents.split())
        return num_words

word_count = get_book_text(book_path) #this assigns a variable to the function's output

print(f"Found {word_count} total words")


