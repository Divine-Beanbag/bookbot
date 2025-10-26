def count_words(book_path): #this function puts all the book_path contents into a variable
    with open(book_path) as f: #opens the book file as a file object
        file_contents = f.read() #stores the contents of the file as
        num_words = len(file_contents.split())
        return num_words

def count_characters(book_path):
    characters = {}
    with open(book_path) as f:
        file_contents = f.read()
        for character in file_contents:
            character = character.lower()
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
        for character in (characters):
            print(f"'{character}': {characters[character]}")
   
    

