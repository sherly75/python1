food_truck1={'name':'Killer Tomato', 'type':'pizza', 'location': 'Ballston'}
food_truck2={'name':'Karnage Asad', 'type':'meat', 'location': 'DC'}
food_truck3={'name':'Country Manners',
             'type':'southern',
             'location': 'ballston'}

#if food_truck['location']=='Ballston'
trucks=[food_truck1,food_truck2,food_truck3]
print(trucks)

food_truck2['is_halal']=True
food_truck1['is_halal']=False
for truck in trucks:
    #print item/dictionary
    #print(truck)
    if truck['location'].lower()=='Ballston'.lower():
        print(truck['name']) #name is a key

    #if key in dict:
    if "is_halal" in truck: #to make sure the key exists otherwise the program wont work
        if truck['is_halal']:
            print(f'{truck["name"]} is halal!')
        else:
            #key exists, but is false
            print(f'{truck["name"]} is Not halal!')
    else:
        #key does not exist
        print('no idea, key does not exist')