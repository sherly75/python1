values =['a','b','c']
#values.append(1)
#values.append(2)
#values.append(3)
values.extend([1,2,3])
print(values)

print(values[2])
#deleting a value : del array_name[index]
del values[1]
print(values)
#values.append(['d','e','f'])
values.extend(['d','e','f'])
print(values) #['d','e','f'] is one single element in case of values.append
#looping through a list
#for singular in plural:
#for one instance in a list
count=0
for value in values: #the word value here is arbitary, u can use any world
    #print(value)
    print(f'value{count}:{value}')
    #count=count+1 ...................
    # for count+=1 can be used for *-/, count*=5
    count+=1


for index, value in enumerate(values):
    print(f'{index}:{value}')
numbers=[1,2,3,4,5,6,7,8,9]
sum=0
for number in numbers:
    sum+=number
print(f'Sum:{sum}')
print(f'avg:{sum/len(values)}')
print(len(values)) #length of the list
#print(list(range(5)))......... NOT IMP RN
for index in range(5):
    print (index)

for index in range(5,10): #range(start,stop) [5,10) 10th index is not included
    print(index)
for index in range(0,21,2):#step or the "2" here is every 2nd number
    print(index)
#alternative loop
#while boolean condition, boolean means some true or false statement has to be executed
index=0
while index<5: #while index is less than 5
    print(index)
    index+=1
else:
    print('done with loop')

while True:
    print('hi')
    break #break exits the loop

message="Hello Marymount"
for letter in message:
    print(letter)
print(message[-1])
#splice
#list_name[start:end]
print(message[0:3])
print(message[6:]) #leaving blank it goes till the end
print(message[:6]) #leaving blank starts at the beginning
food_trucks=['Karnage Asada', ' Killer Tomato', 'Kraving Kabob']
print(food_trucks[1:])
print(food_trucks[-2:])
print(food_trucks[:2])
print('end')

