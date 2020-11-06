
#def funcname(): #def function wont run and everything underneath it
   # print ("Function")

print(1)
print(2)
def say_hi(): #cant start the name with the number
   print("Hi Sherly") # print(4)
    #print(5)

#def say_hi_tina():
#    print('Hi Tina')

count=0
def greet(name):  #def *function* (Parameters, parameters(arguement)):
   print(f'Hi {name}') #name can only be used under this indent........ #name IS A LOCAL SCOPED TO THIS FUNCTION
   #name CANNOT BE SEEN OUTSIDE, i.e. as print(name).
   count=2


print(6)
say_hi()
print(6)
say_hi()
#say_hi_tina()
greet("Tim")
greet('Tina')
greet("John")
print(count)

def greeting (first_name, last_name):
    print(f'Hi {first_name} {last_name}')

greeting("Tim", "Green")
greeting("Sherly", "Pinto")
greeting(first_name="John",last_name="Black")
greeting(last_name='Blue',first_name='Josh')

greeting("Sally", last_name="Pink") #positional should be to the left and keyword should be at the right or it won't work.

def multiply (a,b,c):
 #   print(a*b)
 #print() without return give out  "none"
    return a*b*c  #if u need to use the value again in later calculations.. i.e. remember it in the system

result=multiply(10,2,3)
print(result)

def pizza(*topping, customer): #overloading #cannot customer after *topping as it is unlimited
    print(f'Your pizza has...{topping}')
    print(f'Your pizza has... Specific topping {topping[1]}')
    print(f"{customer}'s pizza has:")
   # print(topping[0])
    #print(topping[1])
    #print(topping[2])
    for ingredient in topping:
        print(ingredient)

pizza("Pepperoni", "Olive", "Banana Peppers", customer="Sherly")

def add_numbers(*numbers):
    summation=0
    for number in numbers:
        summation+=number
    print(f"The sum of the numbers is: {summation}")
    print(summation)

add_numbers(1,2,3,4,5,6,7,8,9)
add_numbers(9,8,7)

def say_hi(first_name="John",last_name="Doe"): #doe if they dont have a last name, give default value via the equal sign
    print(f"Hi {first_name} {last_name}")
say_hi("sherly", "pinto")
say_hi() #default value
say_hi("septina") #if they dont have last name

