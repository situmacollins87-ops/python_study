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

#program that checks if a variable student_score is greater than 90.if true, check if the attendance is greater than 80. if both conditions are true, print 'excellent student' otherwise print 'Good score but attendance needs improvement' always remeber wher you place the else whther innner or outer
student_score=99
attendance=80
if student_score>90:
   if attendance>80:
       print("Excellent student")
   else:
    print('good score but attendance needs improvement')
else:
    print('poor score')

#given x=7 and y =14 write nested conditional statement that xand y are both even if both x and y are even numbers, only y is even if only y is even, neither x nor y are even if both are odd.USE MODULUS
x=5
y=8
if x%2==0:
  if y%2==0:
      print('x and y are both even')
  else:
      print('print x is only even')
else:
    if y%2==0:
        print('only y is even')
    else:
        print('neither x nor y are even')

#Write a program that:
##Takes a transaction amount and account type ("Standard" or "Premium") as input.
##If the account type is "Standard":
##Check if the amount is above 500:
##If it is, print "Transaction exceeds the limit for Standard accounts."
##If not, print "Transaction approved."
##If the account type is "Premium":
##Check if the amount is above 1,000:
##If it is, print "Transaction exceeds the limit for Premium accounts."
##If not, print "Transaction approved."
##Otherwise “Wrong account type
transacation_amount=input('Enter Transaction amount:')
transacation_amount=float(transacation_amount)
account_type=input('enter your account type standard/premium:')
if account_type=='standard':
    if transacation_amount>500:
       print('tranasaction exceeds limit for satndard account')
    else:
        print('transaction approved')
elif account_type=='premium':
    if transacation_amount>1000:
       print("transaction exceeds limit for premium account")
    else: 
        print('transaction approved')
else:
    print('wrong account type')






