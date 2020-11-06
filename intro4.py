"""
can_drive=False

if can_drive:
    print("Must be at least 16")
else:
    print('No drivers license')
"""
age=12
if age>=13:
    print('You can join social media')
    if age>=16:
        print('You can drive')
        if age>=18:
            print('You can vote/buy lottery')
            if age>=21:
                print('You can drink and smoke')
                if age>=25:
                    print('You can rent a car')
                    if age>=35:
                        print('You can be the president')

num=100
if num<5:
    print('less than 5')
elif num<15:
    print('less than 15')
elif num<25:
    print('less than 25')
else:
    print('number must be too high')

name="sherly"
if name=="Sherly":
    print("Hi Sherly")
else:
    print('You are unknown')

if name[0].upper()=='S'and name[-1].upper()=='Y': #Strings work the same way as lists
    print('Your name starts with S and ends with a y')
#elif name[0].upper()=='S': #as python is case sensitive
 #   print('Your first letter is not capitalized')
else:
    print('Your name does not start with S')

import random
number=random.randrange(1,1000)
print(number)
guess=int(input('Give a number between 1-1000'))
#loop until the user guesses correct
#if the number guessed is less, tell them 'you guessed to high'
#if the number guessed is high, tell them "you guessed to low"
#when they do guess it, end the game and tell them they won

#loop while guess is not the number
while guess!=number:
    if guess>number:
        print("You guessed too high")
    else:                                             #elif guess>number: print..
        print("You guessed too low")                    #else print(correct)...
    guess = int(input('Give a number between 1-1000'))
print("You Won! You guessed correct!")



