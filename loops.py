#loops is a programming structure to execute a block of code repeatedly
#allows you to automate repetitive tasks 
#
#used to iterate over a sequence
#syntax for intertaor in sequence:block of code
#iterator is variable that represents each item in a sequence
#syntax correct is block of code then repeated task
fruits=['mango','oranges', 'apple','lemon','grapes ']
for fruit in fruits:
    print('i am a mango')

#display name 10 times
my_list=[1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print('situma')

#in cases of many items eg my name 100 times. You use a range() function which creates a sequence of numbers ie range(start,stop+1)
numbers=list(range(1,101))
for i in numbers:
 print('collo')

 #display numbers between 10 and 50 
 lst=list(range(10,51))
 for num in lst:
    print(num)

#display even numbers between 10 and 50 remember %2==0 displays even
lst4=list(range(10,51))
for num in lst:
   if num %2==0:
      print(num)

#print odd numbers between 30,101
lst3=list(range(30,101))
for m in lst3:
   if m %2!=0:
     print(m)

#storing odd items in empty lists

lst3=list(range(30,101))
odd=[]
for m in lst3:
   if m %2!=0:
      odd.append(m)
print(odd)

#storing even numbers in an empty list
lst4=list(range(10,51))
enve_numbers=[]
for num in lst:
   if num %2==0:
      enve_numbers.append(num)
print(enve_numbers)

#between 1 to 100 display numbers divisible by 3 and 5 in a list
lst5=list(range(1,101))
lst5=[]
for d in lst5:
   if d%3==0 and d%5==0:
       lst5.append(d)
print(lst5)

#SIM pin simulation

lst6=list(range(1,4))
print(lst6)
attempts=3
for i in lst6:
   pin=input('enter your pin')
   correct_pin='0001'
   if pin==correct_pin:
      print('Access Granted')
      break
   else:
      rem_att=attempts-i
      if rem_att==0:
         print('Account blocked')
      else:
         print(f'wrong pin try again you have{rem_att}attempts remaining')
#

