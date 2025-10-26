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
    return characters

def sort_characters(character_count):
    char_list = []

    for character, number in character_count.items():
        if character.isalpha():
            char_list.append({"char": character, "num": number})

    def get_num(num):
        return num["num"]

    char_list.sort(key=get_num, reverse=True)

    return char_list
        
    
            

 
     
             




    





