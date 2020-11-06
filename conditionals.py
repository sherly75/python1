#PART 1)
print('This application determines if the integer entered is a prime or not')

integers=int(input('Enter an integer'))


for index in range(2,integers):
    remainder=integers%index
    if remainder == 0:
        print('The number is not a prime number')
        break
    else:
        print('The integer is a prime number')
        break

#PART 2)
passwords= (input('Please enter your password:'))
#letters
for letter in passwords:
    if len(passwords)<6 and letter.isalpha():
        print('Password is too short, it should be at least 6 characters long and contain at least one number')
        password=(input('Enter password: '))
    else:
        print("Your password meet the requirements! This will be your current approved password.")
