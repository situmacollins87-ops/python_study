fruits=['pawpaw','avacado','mangoes','guava','watermelon']
print(fruits)
#indexing and slicing
print(fruits[2])
print(fruits[0])
#slicing-extracting part of the list
#[start_index:end_index+1]
print(fruits[1:4])
print(fruits[2:5])
#assignment
days_of_the_week=['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(days_of_the_week)
print(days_of_the_week[1:5])
print(days_of_the_week[0])
#Update-first identify index of what you want to update.Using index
fruits[2]='apple'
print(fruits)
#append
fruits.append('lemons')
print(fruits)
#insert
fruits.insert(1,'tomotoe')
print(fruits)

days_of_the_week[3]='Thur'
print(days_of_the_week)
days_of_the_week.append('January')
print(days_of_the_week)
days_of_the_week.insert(2, 'December')
print(days_of_the_week)

#remove
fruits.remove('watermelon')
print(fruits)
#pop
fruits.pop(0)
print(fruits)

days_of_the_week.remove('Friday')
print(fruits)
days_of_the_week.pop(6)
print(days_of_the_week)
days_of_the_week.pop(1)
print(days_of_the_week)
days_of_the_week.clear
print(days_of_the_week)

#Assignment 2
trainees=["John", [2,["James","Mary"]]]
print(trainees[1])
trainees.pop(1)
print(trainees)
trainees.append('56')
print(trainees)
trainees.insert(1,'Mike')
print(trainees)
trainees[1]='8'
print(trainees)
trainees.remove("John")
print(trainees)
print(len(trainees))







