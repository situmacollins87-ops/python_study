my_ds = [45,"Kevin",(720,),["Lesson","Python",{"currency": "KES","student": {"name": "James",
    "age": 23},"subjects": ["Python", "SQL", "HTML", "CSS"]}],834,(91, "Mary", ["HTML", "CSS", "JavaScript"])
]
print(my_ds)
#print KES
print(my_ds[3][2]['currency'])
#print 720 from the tuple. (mine 720 is first item in the tuple so index 0)
print(my_ds[2][0])
#print python from nested list 
print(my_ds[3][1])
#print student's name "James"
print(my_ds[3][2]["student"]["name"])
#print SQL
print(my_ds[3][2]["subjects"][1])
#print html
print(my_ds[3][2]["subjects"][2])
#add a new amount 1500
my_ds[3][2]["amount"]=1500
print(my_ds[3][2])
#change students name from Brian to James
my_ds[3][2]["student"]["name"]="James"
print(my_ds[3][2]["student"])
#add Django to the end of subjects list
my_ds[3][2]["subjects"].append("Django")
print(my_ds[3][2]["subjects"])
#change css to bootstrap
my_ds[3][2]["subjects"][3]="Bootstrap"
print(my_ds[3][2]["subjects"])
