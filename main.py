# --- my first boot.dev project, called bookbot ---

# --- imports ---

from stats import count_words
from stats import count_chars
from stats import sorted_list
import sys

# ---
def check_usage():
    if len(sys.argv) > 1:
        return
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(filepath): # returning the content of a file as string
    with open(filepath, "r") as f:
        content = f.read()
    return content

def text_str(): # writing a  function to print the content
    return str(get_book_text(fp))


def print_char_count():
    for i in sorted_list:
        if i["char"].isalpha():
         print(f'{i["char"]}: {i["num"]}')


def print_report():
    head = f'''============ BOOKBOT ============\nAnalyzing book found at {fp}...'''
    word_count = f'''----------- Word Count ----------\nFound {num_words} total words'''
    char_count = f'''--------- Character Count -------'''
    end = "============= END ==============="

    print(f'{head}\n{word_count}\n{char_count}')
    print_char_count()
    print(end)




check_usage()

fp = sys.argv[1]

num_words = count_words(text_str())
char_dict = count_chars(text_str())
sorted_list = sorted_list(char_dict)

print_report()