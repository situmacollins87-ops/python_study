#series of if in another if
#nested if depends on result of previous condition
#eg a drivers license can be issued to 18 year old and above else not legible 
age=input('enter your age:')
age=int(age)
if age>=18:
    license=input('do you have a drivers license yes/no?')
    if license=='yes':
        print('Eligible to drive')
    else:
        print('not elible to drive')
else:
    print('you are too young to drive')

    #credit score
credit_score=input('Enter your credit score')
annual_income=('Enter your annual income')

if credit_score>700:
    if annual_income>50000:
       print('loan approved')
else:
    print('credit score too low')

#program that checks if a variable student_score is greater than 90.if true, check if the attendance is greater than 80. if both conditions are true, print 'excellent student' otherwise print 'Good score but attendance needs improvement'
student_score=99
attendance=80
if student_score>90:
   if attendance>80:
       print("Excellent student")
else:
    print('good score but attendance needs improvement')

#given x=7 and y =14 write nested conditional statement that xand y are both even if both x and y are even numbers, only y is even if only y is even, neither x nor y are even if both are odd
x=5
y=8
if x==2:
  if y==2:
      print('x and y are both even')
else:
    if y==2:
        print('only y is even')
    else:
        print('neither x nor y are even')




