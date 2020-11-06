user={'first_name':'Sherly','last_name':'Pinto','age':19}
print(user)

print(f'Hello {user["first_name"]} you are {user["age"]}')

user['age']=20
print(f'Hello {user["first_name"]} you are {user["age"]}')

#to add
#dictionary[new_key]=value
user['email']='sjp20002@marymount.edu'
print(user)
#del dict[key] removes that key/value pair
del user['age']
print(user)
#print(user[0]) wont work because it is looking for a key named "0"
user['favorite_foods']=['pizza', 'ice cream', 'cookies'] #a list within a dictionary
print(user)
print(user['favorite_foods'][0][-1]) #first food and last Letter of the first item. so it prints only the last letter


print(user.keys())
for key in user.keys():
    print(f'{key}: {user[key]}')

print(user.values())

for key,value in user.items():
    print(f'{key}: {value}')
