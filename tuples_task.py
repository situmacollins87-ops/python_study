numbers=(10,20,30,40,50)
#add 60 at end and replace 30 with 35
#first point is to convert to list
numbers=list(numbers)
#modify
numbers.append('60')
numbers[2]=35
#bring back to tuple
numbers=tuple(numbers)
print(numbers)
#2
values=(15,5,30,25,10)
#arrange in ascending order
values=list(values)
values.sort()
values=tuple(values)
print(values)
fruits=('apple','banana','cherry','banana','mango','banana')
#findthe occurrence of banana
fruits=list(fruits)
print(fruits.count('banana'))
fruits=tuple(fruits)
#remove mango
fruits=list(fruits)
fruits.remove('mango')
fruits=tuple(fruits)
colours=('red','blue','green')
#add yellow at index 1
colours=list(colours)
colours.insert(1,'yellow')
colours=tuple(colours)
print(colours)