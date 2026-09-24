my_ds = [23, 'Jane', (560), ['Lesson', 'Maths', {'currency' : 'KES'}], 987, (76,'John')]
print(my_ds)
#print KES
print(my_ds[3][2]['currency'])
print(my_ds)
#print 560
print(my_ds[2])
#print maths
print(my_ds[3][1])
#add aount 90 in dictionary
my_ds[3][2]['amount']=90
print(my_ds)
#reverse 987 to 789 without using inbuilt method:Hint strings must be reversed using [::]
print(my_ds[4])
#convert to string
my_ds[4]=str(my_ds[4])
my_ds[4]=my_ds[4][::-1]
my_ds[4]=int(my_ds[4])
print(my_ds)
#change name John to Jane
print(my_ds[5][1])
my_ds[5]=list(my_ds[5])
my_ds[5][1]='Jane'
my_ds[5]=tuple(my_ds[5])
print(my_ds)

