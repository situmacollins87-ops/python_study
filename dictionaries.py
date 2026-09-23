#Dictionaries
#enclosed with curly brace{}
#keys are always strings but the values can be of any type
#keys are always unique
#have no index as such we use keys to acces values 
student1={
    "name":"Collins",
    "age" :"37",
    'County':'Nairobi',
    "gender":"Male",
}
print(student1["County"])
#Add key an value
student1['tribe']='Luhya'
print(student1['tribe'])
#Update
student1['tribe']='Teso'
print(student1['tribe'])