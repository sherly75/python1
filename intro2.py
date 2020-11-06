#Strings
first_name='Sherly'
#integers
age=39
#float
pi=3.14
#booleans T/F
can_drive=True
#can_drive="Yes I can"

#arthmetic
#concatination "hi" + "world"
a=10
b=5
#FOLLOWS PEMDAS/BODMAS
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #modulus command, i.e. remainder command
print(a%2) #even leaves a remainder 0
print(b%2) #to check if even or odd. odd leaves remainder 1
print((a*b)/(b/2))

bmi=a*b
print(bmi)

#LISTS LIKE Arrays in JAVA; list var_name=[value1, value2]
team=["Washington", "Redskins", "DC", 3, 13] #team=[0,1,2,3,4]
print (team)
#access in a list [index]
print(team[1])
print(f'Team Name: {team[0]}')
print(f'Team Nickname: {team[1]}') #f means formatted

#change of value
#var_name[index] = new value
team[0]="Virginia"
team[2]="Arlington"


#adding more values
team.append("Ashburn National Stadium")
team.append("Gruden")
print(f'Coach: {team[6]}')
print (f'Coach: {team[-1]}') #negative index for reversible index finding [from last]

print(team)
team1=["Carolina", "Panthers", "NC", 5, 11, "BoA", "Rivera"] #team=[0,1,2,3,4] BoA=Bank of America
print(team1)
nfl=[team, team1]

print(nfl)
print(nfl[1])
print(nfl[0][1])
print(nfl[1][1])
print(nfl[-1][-1])
