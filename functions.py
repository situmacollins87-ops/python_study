#custom functions
#don't add any logic
#only arrange code into reusable blocks
#creating custom functions
#define function using the def keyword
#followed by the name
#syntax below
#def function_name():
#block of code

#are of a square using a function
def square_area():
    side=10
    side=10
    area=side*side
    print(area)
square_area()

#area of circle
def circle_area():
    pi=3.14
    radius=20
    area=pi*radius*radius
    print(area)
circle_area()
#parameters are variables used inside a function
#arguments are exact values passed when calling a function
def square_area(side):
    area=side*side
    print(area)
square_area(10)

#funstion that calculates area of rectangle 
def rectangle_area(lenght,width):
    area=lenght*width
    print(area)
rectangle_area(20,10)