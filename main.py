from stats import get_number_of_words
from stats import get_freq_of_xter
from stats import get_sorted_dict
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
        return file_contents


#Usage: python3 main.py <path_to_book>

def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    num_words = get_number_of_words(content)
    dict_xter = get_freq_of_xter(content)
    dict_sorted = get_sorted_dict(dict_xter)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in dict_sorted:
        if (i['key'].isalpha()):
            print(f"{i['key']}: {i['value']}")
    print("============= END ===============")
        
    
   
   

main()
