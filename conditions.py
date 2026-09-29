#proper handwritten notes in book
#conditions excute ablock of code only when condition is true
#syntax if cindition:#block of code
if 20>100:
    print('twenty is greater')
age=50
print(age)

if age>18:
    print('Adult')
age=20
print(age)

#authorize user with age from 18 to 60
if age>=18 and age<=60:
    print('Allow Access')
age=58
print(age)

#check temeperature above 30 print too hot
temperature=45
if temperature>30:
   print('too hot')
print(temperature)

if 20>100:
 print('twenty is greater')
else:
   print('twenty is less')
age=18
print(age)

if age>18:
   print('Adult')
else:
   print('Minor')
age=12
print(age)

#pass if student marks is above 50 else fail
marks=40
if marks>=50:
   print('Pass')
else:
   print('fail')
print(marks)

#print senior Adult if age is above 50, print if age is above 20, print teenager if age is above 12 otherwise print child 
age=2
if age>50:
   print('senior adult')
elif age>20:
   print('adult')
elif age>12:
   print('teenager')
else:
   print('child')
print(age)

marks=30
if marks>80:
   print('A')
elif marks>70:
   print('B')
elif marks>60:
   print('C')
elif marks>50:
   print('D')
else:
   print('fail')
print(marks)

