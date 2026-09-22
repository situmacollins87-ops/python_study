#just like list they store multiple items of different data types
fruits=('bananas', 'Oranges', 'Bananas', 'Grapes')
print(type(fruits))
print(fruits[2])
print(fruits[1:4])
#convert to list if you relaly have to modify anything in class tuple
fruits=list(fruits)
print(fruits)
#convert back to tuple using tuple function
fruits=tuple(fruits)
print(fruits)
#task
days=('Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday')
days=list(days)
print(days)
print(days[2])
print(len(days))
days[3]='Thur'
print(days)
days=tuple(days)
print(days)
