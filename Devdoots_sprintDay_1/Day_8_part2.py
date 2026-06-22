#Question 1: Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.


f = open("poems.txt", "r")
content = f.read()

if "twinkle" in content.lower():
    print("twinkle world is present in content")
else:
    print("NO, twinkle world is not present")

f.close()

# Question 2: The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

def game():
    return 95

score = game()

f = open("Hi-score.txt", "r")
hiscore_data = f.read().strip() 
f.close()


if hiscore_data == "":
    hiscore = 0
else:
    hiscore = int(hiscore_data)


if score > hiscore:
    print(f"New High score broken! Previous was {hiscore}, New is {score}")
    
    f = open("Hi-score.txt", "w")
    f.write(str(score))
    f.close()
else:
    print(f"High score are not broken. Current Score: {score}, High Score: {hiscore}")


# Question 3: Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old

import os

if not os.path.exists("tables"):
    os.mkdir("tables")

for i in range(2, 21):
    table_content = ""  

    for j in range(1, 11):
        table_content += f"{i} X {j} = {i*j}\n"

    file_name = f"tables/table_{i}.txt"
    f = open(file_name, "w")
    f.write(table_content)
    f.close()

print("My_Table!")


# Question 4: A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating the same file.

f = open("censor.txt", "r")
content = f.read()
print(content)
f.close()

New_content = content.replace("Donkey", "####")

f = open("censor.txt", "w")  
f.write(New_content)
f.close()


#Question 5: Repeat program 4 for a list of such words to be censored.


f = open("censor_list.txt", "r")
content = f.read()
print(content)
f.close()

words_list=["donkey","bad","stupid"]

for word in words_list:

    New_content=content.replace("word","####")

    f = open("censor_list.txt", "w")  
    f.write(New_content)
    f.close()

# Question 6: Write a program to mine a log file and find out whether it contains ‘python’ or not.

f = open("log.txt", "r")
content = f.read()
f.close()

if "python" in content:
    print("Checking your log file...")
    print("Result: Yes! Lower.")

elif "Python" in content:
    print("Checking your log file...")
    print("Result: Yes! Uppercase '.")

else:
    print("Checking your log file...")
    print("Result: No, 'python' word is not found in this file.")

   
# Question 7: Write a program to find out the line number where the word 'python' is present in a log file.#  
   
f = open("log.txt", "r")
lines = f.readlines()
f.close()

line_no = 1

for line in lines:
    if "python" in line: 
        print(f"Yes! Python word is present on line number: {line_no}") 
    
    line_no += 1   


# Question 8: Write a program to make a copy of a text file.


f = open("log.txt", "r")
content = f.read()
print(content)
f.close()


f = open("log_copy.txt", "w")  
f.write(content)
f.close()


print("File copied successfully! Check your sidebar for log_copy.txt")


# Question 9: Write a program to find out whether a file is identical & matches the content of another file.

f = open("log.txt", "r")
file1_data = f.read()
print(content)
f.close()

f = open("log_copy.txt", "r")
file2_data  = f.read()
print(content)
f.close()

if file1_data == file2_data:
    print("YES,Python world is content")
    
    
else:
    print("NO,Python world is not content")


# Question 10: Write a program to wipe out the contents of a file using Python.

f = open("log_copy.txt", "w")  
f.close()

print("File content has been wiped out successfully! ")

#Question 11: Write a program to rename a file to "renamed_by_python.txt" using Python.

import os
os.rename("log_copy.txt","rename _br_python.txt")

print("File has been renamed successfully by Python! ")