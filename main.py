#Import sys
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read() 
        return file_contents
    
from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_list

def main():

    if len(sys.argv) == 2:
        
    

        path = sys.argv[1]
        file_contents = get_book_text(path)
        num_words = get_num_words(file_contents)
        #print(f"{num_words} words found in the document")
        #print(get_char_count(file_contents))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        sorted_dict = get_sorted_list(file_contents)
        for value in sorted_dict:
            print(f"{value['char']}: {value['num']}")
        print("============= END ===============")
        return sys.exit(1)

    else:
        print("Usage: python3 main.py <path_to_book>")

main()