#This approach allows for reading files line by line - eliminates issues with huge files being loaded to the RAM
#re used to break up sentence into words - either by commas or spaces - avoids errors with deleting single words
import re

def print_document(file):
    with open(file, 'r', encoding="utf-8") as txt:
        for line in txt:
            print(line)

def remove_words_logic_file(filter_words, txt):
    remove_count = 0

    for line in txt: #load line
            line_words = re.split(r'[, ]', line) #creates a list of words in sentence
            for word in line_words:
                for sub_str in filter_words: #Check each filter word
                    if sub_str == word:
                        print(f"sub_str: {sub_str}")
                        line_words.remove(sub_str)
                        remove_count += 1
                    line = " ".join(line_words)
            print(line)
    
    return remove_count

def remove_words_logic_str(filter_words, input_str):
    remove_count = 0

    for line in input_str.splitlines(): #load line
            line_words = re.split(r'[, ]', line) #creates a list of words in sentence
            for word in line_words:
                for sub_str in filter_words: #Check each filter word
                    if sub_str == word:
                        print(f"sub_str: {sub_str}")
                        line_words.remove(sub_str)
                        remove_count += 1
                    line = " ".join(line_words)
            print(line)
    
    return remove_count

def remove_words(filter_words, input_str):
    #This function prepares input for logic
    #filter_words - filter sentences
    #input_str - filepath or input string

    remove_count = None
    print(f"Words to remove [FILTER]: {filter_words} \n Filtered (removed) sentence: \n|\n|\nv")
    
    try:
        #input is a file case
        with open(input_str, 'r', encoding="utf-8") as txt:
            remove_count = remove_words_logic_file(filter_words, txt)
    except:
        #input is a string from console case
        remove_count = remove_words_logic_str(filter_words, input_str)
        
    try:
        print("removed words: ", remove_count)
    except Exception as e:
        print(f"remove_words error: {e}")

    

if __name__ == "__main__":
    #input string filepath
    doc = 'text.txt'
    #remove filter
    rem_words = ['się', 'oraz', 'nigdy', 'dlaczego', 'i']

    print(f"------\n1. Provide input string\n2. Provide input file\n3. Enter demonstration mode [requires {doc} file]")

    choice = input()

    match choice:
        case "1":
            print("Provide your direct input text:\n")
            str_in = input()
            print(f"--------\nInput text: ")
            print(str_in)
            remove_words(rem_words, str_in)
        case "2":
            print("Provide filepath to your txt file")
            str_in = input()
            try:
                print(f"--------\nInput text: ")
                print_document(str_in)
                remove_words(rem_words, str_in)
            except Exception as e:
                print(f"File path mode error: {e}")
        case "3":
            print(f"Enter demonstration mode [requires {doc}]")
            print(f"--------\nInput text: ")
            print_document(doc)
            remove_words(rem_words, doc)
        case _:
            print("wrong choice")
            
    print("---------")