#Project 1
image=input("Enter the character(s) that will compose the pyramid: ") #Define the characters that will be used in the pyramid
levels=int(input("Enter how many levels the pyramid should have: ")) #Define the number of levels of the pyramid
if levels <= 0: #In case the user enters 0 for number of levels
    print("Error: Pyramid has been defined with zero levels.") #0 error message
elif levels > 0: #For all integer levels above 0
    for i in range(1,levels+1): #Defining the range of each level
        print(i*image) #Print the result
else: #In case the user enters a non-integer for number of levels
    print("Error: Pyramid levels have not been defined with an integer.") #Non-integer error message

#Project 2
image=input("Enter the character(s) that will compose the pyramid: ") #Define the characters that will be used in the pyramid
levels=int(input("Enter how many levels the pyramid should have: ")) #Define the number of levels of the pyramid
if levels <= 0: #In case the user enters 0 for number of levels
    print("Error: Pyramid has been defined with zero levels.") #0 error message
elif levels > 0: #For all integer levels above 0
    for i in range(levels): #Defining the range of each level and making them skip even numbers
        print(" "*(levels-i-1)+image*(2*i+1)) #Print the characters and the spaces in the right format
else: #In case the user enters a non-integer for number of levels
    print("Error: Pyramid levels have not been defined with an integer.") #Non-integer error message

#Project 3
image=input("Enter the character(s) that will compose the pyramid: ") #Define the characters that will be used in the pyramid
levels=int(input("Enter how many levels the pyramid should have: ")) #Define the number of levels of the pyramid
if levels <= 0: #In case the user enters 0 for number of levels
    print("Error: Pyramid has been defined with zero levels.") #0 error message
elif levels > 0: #For all integer levels above 0
    for i in range(levels): #Defining the range of each level and making them skip even numbers
        print(" "*len(image)*(levels-i-(1))+image*(2*i+1)) #Print the characters and the spaces in the right format
else: #In case the user enters a non-integer for number of levels
    print("Error: Pyramid levels have not been defined with an integer.") #Non-integer error message

#Project 4
range1=int(input("Enter the minimum value of the range of the parabola: ")) #Define the minimum range of the parabola
range2=int(input("Enter the maximum value of the range of the parabola: ")) #Define the maximum range of the parabola
scale=int(input("Enter the scaling factor for the parabola: ")) #Define the scaling factor of the parabola
if range1>range2: #In case the user inputs a minimum range greater than the maximum
    print("Error: Minimum value of range larger than maximum value.") #Minimum > Maximum error message
elif range1<=range2: #For all functional ranges
    for i in range(range1,range2+1): #Defining the range of the parabola
        print(" "*(abs(i)*(scale+2)+(abs(i)^-1)),".") #Printing a number of spaces relative to the range and scale of the parabola, followed by a point, on each line
else: #In case of any other errors
    print("Error: Integer value not properly defined.") #One or more of the values was not properly defined as an integer

#Project 5
radius=int(input("Enter the value of the radius: ")) #Defining the radius of the circle
for i in range(-radius,radius+1): #Defining the size of the circle
    print(" "*(abs(i)*3+(abs(i)^-1)),"."," "*4*(abs(i)*(-1)+(radius)),".") #Priting a series of spaces and points relative to the radius of the circle
