# Lab 3 Text Processing

### 1. Write a script that removes from an input text (direct input or from a txt file) the following words: **się, i, oraz, nigdy, dlaczego**

### 2. Write a script that, in a given input, replaces the words **i, oraz, nigdy, dlaczego** with **oraz, i, prawie nigdy, czemu** respectively. Suggested structure: a dictionary.

# Answers:

## [Ad. 1](ex1.py)
```bash
lab4 % python3 ex1.py
------
1. Provide input string
2. Provide input file
3. Enter demonstration mode [requires text.txt file]
4. Exit
1
Provide your direct input text:

się nigdy oraz próba i THE END
--------
Input text: 
się nigdy oraz próba i THE END
Words to remove [FILTER]: ['się', 'oraz', 'nigdy', 'dlaczego', 'i'] 
 Filtered (removed) sentence: 
|
|
v
nigdy próba THE END
removed words:  3
---------
------
1. Provide input string
2. Provide input file
3. Enter demonstration mode [requires text.txt file]
4. Exit
3
Enter demonstration mode [requires text.txt]
--------
Input text: 
L1 slowo, się, slowo, i, slowo, oraz, slowo, nigdy, slowo, dlaczego, slowo

L2 slowo, się, slowo, i, slowo, oraz, slowo, nigdy, slowo, dlaczego, slowo

L3 KONIEC PLIKU
Words to remove [FILTER]: ['się', 'oraz', 'nigdy', 'dlaczego', 'i'] 
 Filtered (removed) sentence: 
|
|
v
L1 slowo   slowo   slowo   slowo   slowo   slowo

L2 slowo   slowo   slowo   slowo   slowo   slowo

L3 KONIEC PLIKU
removed words:  10
---------
------
1. Provide input string
2. Provide input file
3. Enter demonstration mode [requires text.txt file]
4. Exit
4
Quitting the program loop
lab4 %
```

## [Ad. 2](ex2.py)
```bash
lab4 % python3 ex2.py   
------
1. Provide input string
2. Provide input file
3. Enter demonstration mode [requires text2.txt file]
4. Exit
3
Enter demonstration mode [requires text2.txt]
--------
Input text: 
L1 dlaczego, nigdy oraz i 

L2 slowo, się, slowo, i, slowo, oraz, slowo, nigdy, slowo, dlaczego, slowo

L3 KONIEC PLIKU
Words to switch [FILTER]: {'i': 'oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy', 'dlaczego': 'czemu'} 
 Filtered (switched) sentence: 
|
|
v
L1 czemu  prawie nigdy i oraz 

L2 slowo  się  slowo  oraz  slowo  i  slowo  prawie nigdy  slowo  czemu  slowo

L3 KONIEC PLIKU
Switched cases:  8
---------
------
1. Provide input string
2. Provide input file
3. Enter demonstration mode [requires text2.txt file]
4. Exit
4
Quitting the program loop
lab4 %
```