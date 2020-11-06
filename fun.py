"""
import os
with open ("test.txt") as myfile: #Gives back a list
    contents=myfile.readlines()
print (contents)

with open ("test.txt", encoding="utf8") as myfile: #Give back string #encoding covers most languages letter and stuff beyond english alphabets (mode)
    filecontents=myfile.read()
print (filecontents)


#read in pi,txt
#ask user for birth is format
with open ("Data"+os.sep+"pi.txt") as pifile: #os.sep adds seperator
    pi=pifile.read()
    print(pi)
birthday=input('Please enter your birthday in (MM/DD) format:')
if birthday in pi:
    print('Yes')
else:
    print('No')
"""
#r =read
#w = write
#a = append when you do not want to over-write a file

with open ("out.txt", "a") as mymoutputfile:
    mymoutputfile.write('Hello Marymount\n')
    mymoutputfile.write('Goodbye Marymount')
#divide=age/birthday
#print(f'Your age in pi= {divide}pi')
"""
food = ['apple\n', 'banana\n', 'carrot\n', 'donut\n']
with open("food.txt", 'w') as outfile:
    outfile.writelines(food)
"""
food = ['apple', 'banana', 'carrot', 'donut']
with open("food.txt", 'w') as outfile:
    #outfile.writelines(food)
    outfile.write(" \n".join(food)) #forms a string with anything in the "" is placed between each thing in the list

#string="hello\n"
#String.strip() strip will remove anny line breaks for you #break words
mystring="The Cat in the hat"
words = mystring.split(" ")
print(words)

"""
     if texts[text]<124707:
     print (texts, texts[text])

    import operator
    sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))import operator  
"""