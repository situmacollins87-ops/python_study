sentence1= "   JOHn"
sentence1=sentence1.strip()
print(sentence1.lower())
sentence2="The Dog Breed is German Shephered"
sentence2=sentence2.replace('The','')
sentence2=sentence2.replace('Dog','')
sentence2=sentence2.replace('Shephered','')
print(sentence2)
#On above use slicing method
sentence3="Defeats for the Clinton forces , this was her moment of triumph"
print(sentence3[16:30])
#On above use the split method
sentence4="The lazy dog; ran so fast; it hit a wall"
sentence4=sentence4.split(';')
print(len(sentence4))
first_name=" Joh.n"
last_name=" Do,e"
first_name=first_name.strip()
first_name=first_name.replace(".", "")
last_name=last_name.strip()
last_name=last_name.replace(",","")
full_name=first_name + last_name
full_name= first_name+" "+last_name
print(full_name)