import re

def print_document(file):
    with open(file, 'r', encoding="utf-8") as txt:
        for line in txt:
            print(line)


def remove_words(words, file):
    remove_count = 0
    print(f"Words to remove [FILTER]: {words} \n Filtered (removed) sentence: \n|\n|\nv")

    with open(file, 'r', encoding="utf-8") as txt:
        for line in txt: #load line
            temp = line
            temp = re.split(r'[, ]', temp) #split for words
            #Add checking for each word, not for line (issue with 'i' removal from nigdy)
            for sub_str in words:
                if sub_str in line:
                    line = line.replace(sub_str,'')
                    remove_count += 1
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


        

        
