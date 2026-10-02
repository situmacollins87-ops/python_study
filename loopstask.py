#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
lst7=list(range(1,4))
print(lst7)
attempts=4
for i in lst7:
   pin=input('enter password')
   correct_pin='admin@123'
   if pin==correct_pin:
      print('Access Granted')
      break
   else:
      rem_att=attempts-i
      if rem_att==0:
         print('Account blocked')
      else:
         print(f'wrong password try again you have{rem_att}attempts remaining')

#Write a program that displays a numbers 1 to 50 inside a list.
#From 1 above display the ones divisible by 7 or 5 inside a list.
#Find sum and average of values in the range between 10 to 40.
#Put in a list the first 10 odd numbers between 10 to 50. 
#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
#ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
#Display the total quantity of the 3 above.
numbers_1_to_50 = list(range(1, 51))
print("1. Numbers 1 to 50:")
print(numbers_1_to_50)
print("-" * 50)



