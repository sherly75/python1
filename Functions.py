#default(firstname, lastname, age)=("John", "Doe", 18)
def calculate_dog_years(firstname="John", lastname="Doe", age=18):
    dog_years = 7 * age
    print(f'Hi {firstname.capitalize()} {lastname.capitalize()}, you may be {age} years old but in dog years you are {dog_years} years old so get busy living!')

#firstname = input("Enter your first name \n" )
#lastname = input("Enter your last name \n" )
#age = int((input("Enter your age \n" ))


calculate_dog_years("sherly", "pintowq", 19)

# calculate_dog_years(firstname="John", lastname="Doe", age=18)
#part 2
#is_prime(N)


def is_prime(N):
    for integer in range(2,(N)):
        if N%integer==0:

            return False
            #break
        else:
            return True
            #break
if is_prime(13)==True:
    print("Prime number")
else:
    print("Not a prime number")



