#Take as input from useer the temperature if the temperature is above 30 disppaly 'the temperature is too hot if the temperature is above 15 display Normal temperature otherwise display cold temperature
temperature=15
if temperature>30:
    print('too hot')
elif temperature>15:
    print('normal temperature')
else:
    print('too cold')

#write python program that checks if a variable X is between 10 and 20(inclusive) and if another variable y is greater than 100. If both conditions are met otherwise print conditions not met
x=1
y=25
if 10<=x<=20 and y>100:
    print("conditions met")
else:
    print("conditions not met")

#python program that checks if variable password is equal to the string "secret 123". if it is print "Access granted" otherwise print "Access denied"
password='secret 123'
if password=='secret 123':
   print('Access granted')
else:
    print('Access denied')
#Assume start date = 2024-01-01 and end date =2024-12-31 write a conditional statement taht checks, if date comes befor eend date print valid date, if date comes after valid date print invalid date if dates aresame print one-day period
start_date=(2024-1-1)
end_date=(2024-12-31)
if start_date<end_date:
    print('valid period')
elif start_date>end_date:
    print('invalid period')
else:
    print('one day period')
print(start_date)

#strings 
str1="collins"
str2="Methusellah"
if len(str1)>len(str2):
    print('str1 is longer')
elif len(str2)>len(str1):
    print('str2 is longer')
else:
    print('both are of equal lenghth')
print(str)

#last
valid_ids=[101,102,103]
user_id=105
if user_id in valid_ids:
    print('Access granted')
else:
    print('Access denied')

