#This approach allows for reading files line by line - eliminates issues with huge files being loaded to the RAM
#re used to break up sentence into words - either by commas or spaces
import re

def print_document(file):
    with open(file, 'r', encoding="utf-8") as txt:
        for line in txt:
            print(line)


def remove_words(filter_words, file):
    #filter_words - filter sentences
    #file - filepath

    remove_count = 0
    print(f"Words to remove [FILTER]: {filter_words} \n Filtered (removed) sentence: \n|\n|\nv")

    with open(file, 'r', encoding="utf-8") as txt:
        for line in txt: #load line
            line_words = re.split(r'[, ]', line) #creates a list of words in sentence
            #print(f"len(line_words) = {len(line_words)}, print(line_words) = {line_words}")
            for word in line_words:
                for sub_str in filter_words: #Check each filter word
                    if sub_str == word:
                        #print(f"substr FOUND, Word: {word}, thing to remove: {sub_str}")
                        line_words.remove(sub_str)
                        #word = word.replace(sub_str,'')
                        remove_count += 1
                    #print("substr NOT FOUND")
                    line = " ".join(line_words)
            print(line)
            

    print("removed words: ", remove_count)
    

if __name__ == "__main__":
    #input string filepath
    doc = 'text.txt'
    #remove filter
    rem_words = ['się', 'oraz', 'nigdy', 'dlaczego', 'i']


    print(f"--------\nInput text: ")
    print_document(doc)
    print("---------")

    remove_words(rem_words, doc)


        

        
