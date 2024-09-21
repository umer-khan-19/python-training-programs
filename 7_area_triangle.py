"""
In the below line of code we take input from user, using input and convert it into float numbers.
and using map funtion we can take input in one line and assign it into two variables using split function.
spilt() function basically doing split the input in the basis of apacing.
split()  splits the input string at spaces by default (you can specify other delimiters if needed).
"""
height,breadth = map(float,input("Enter height and breagth by spacing between them for calculating the area of triangle:").split())
area_of_a_triangle = 0.5*height*breadth
print(area_of_a_triangle)