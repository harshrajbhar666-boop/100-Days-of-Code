#write a python program to display a user enterd named by followed by good afternoon using input function  is ko hinglish ma batao 

name=input("Enter your name: ")

print("GOOD AFTERNOON")

# write a program to fill in a letter template given below with name and date

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

name=input("Enter your name:")
date=input("Enter your Date:")

letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)

# write a program to detect double space in astring 

text="This is a string with double spaces"

index=text.find("")
print("Double space is at index:", index)

# Replace the double space from problam 3 with single spaces

text="This is a string with double spaces"
index=text.replace("","")

print("text")

# write a program to formate the following letter using escape sequence character

letter="Harsh is a good boy,\nBut Harsh's nature is not good."

print(letter)




