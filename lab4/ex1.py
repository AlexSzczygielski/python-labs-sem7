#This approach allows for reading files line by line - eliminates issues with huge files being loaded to the RAM
#re used to break up sentence into words - either by commas or spaces - avoids errors with deleting single words
import re
import os

def print_document(file):
    with open(file, 'r', encoding="utf-8") as txt:
        for line in txt:
            print(line)


def remove_words_logic(filter_words, line):
    #Requires a single line as an input!
    #List (many lines) input will raise an error
    remove_count = 0

    line_words = re.split(r'[, ]', line) #creates a list of words in sentence
    for word in line_words: #Check each word in line with filter
        if word in filter_words:
            #print(f"removing: {word}")
            line_words.remove(word)
            remove_count += 1
    line = " ".join(line_words)
    print(line)
    
    return remove_count


def remove_words(filter_words, input_str):
    #This function prepares input for logic
    #filter_words - filter sentences
    #input_str - filepath or input string
    print(f"Words to remove [FILTER]: {filter_words} \n Filtered (removed) sentence: \n|\n|\nv")

    remove_count = 0
    lines = None
    
    try:
        #input is a file case
        with open(input_str, 'r', encoding="utf-8") as txt:
            for line in txt:
                remove_count += remove_words_logic(filter_words, line)
    except FileNotFoundError:
        #input is a string from console case
        lines = input_str.splitlines()
        for line in lines:
            remove_count += remove_words_logic(filter_words, line)
        
    try:
        print("removed words: ", remove_count)
    except Exception as e:
        print(f"remove_words error: {e}")

    

if __name__ == "__main__":
    #input string filepath
    doc = 'text.txt'
    #remove filter
    rem_words = ['się', 'oraz', 'nigdy', 'dlaczego', 'i']

    while(True):
        print(f"------\n1. Provide input string\n2. Provide input file\n3. Enter demonstration mode [requires {doc} file]\n4. Exit")

        choice = input()

        match choice:
            case "1":
                print("Provide your direct input text:\n")
                str_in = input()
                if os.path.isfile(str_in):
                    print("Provided input is a file!")
                else:
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
                    print(f"Mode 2, filepath mode error: {e}")
            case "3":
                print(f"Enter demonstration mode [requires {doc}]")
                print(f"--------\nInput text: ")
                print_document(doc)
                remove_words(rem_words, doc)

            case "4":
                print("Quitting the program loop")
                break

            case _:
                print("wrong choice")        
        print("---------")