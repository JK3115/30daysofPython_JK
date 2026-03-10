#Exercises Day 3

# 1 - Declare your age as integer variable.
age='37' 
# 2 - Declare your height as a float variable.
height=6.1 
# 3 - Declare a variable that stores a complex number.
complex_number=complex(1+2j)

# 4 - Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle.
base=int(input("Enter base dimension: "))
height=int(input('Enter height dimension: '))
area_of_triangle= (0.5 * base * height)
print("The area of the triangle is ", area_of_triangle)

# 5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle.
side_a=int(input('Enter side a: '))
side_b=int(input('Enter side b: '))
side_c=int(input('Enter side c: '))
perimeter_of_triangle=side_a+side_b+side_c
print("The perimeter of the triangle is: ",perimeter_of_triangle)

# 6 - Get length and width of a rectangle using prompt. Calculate its area and perimeter.
length=int(input("Enter length: "))
width=int(input('Enter width: '))
area_rectangle=length*width
perimeter_rectangle=2*(length+width)
print("The area of the rectangle is", area_rectangle, "and the perimeter is ", perimeter_rectangle)

# 7 - Get radius of a circle using prompt. Calculate the area and circumference.
radius=int(input("Enter radius:"))
pi=3.14
area_circle=pi*radius*radius
circumference=2*pi*radius
print("The area of the circle is ", area_circle, "and the circumfernce is ",circumference)

# 8 - Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("Slope = 2")
print("x-intercept = 1")
print("y-intercept = -2")

# 9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,y1,x2,y2=2,2,6,10
slope=(int((y2 - y1)/ (x2 - x1)))
print("The slope is ", slope)
print(f"The Euclidean distance {((x2-x1)**2 + (y2-y1)**2) ** 0.5:.2f}")

# 10 - Compare the slopes in tasks 8 and 9.
print(2 == slope)

# 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range (-10,10):
    y=((x**2)+6*x+9)
    if y== 0:
        print("Y is 0 when X is ", x)
        break # Solution is Y is 0 when x = -3
    else:
        print("X value is not in range")

# 12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print((len('python')) is not (len('dragon')))

# 13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

# 14 - I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("on" in "I hope this course is not full of jargon.")

# 15 - "There is no 'on' in both dragon and python"
print("on" not in "python" and "on" not in "dragon")

# 16 - Find the length of the text python and convert the value to float and convert it to string
print(str(float(len("python"))))

#17 - Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
User_input=(int(input("Enter number to test even or odd ")))
print("Even " if (User_input)%2 ==0 else "odd")

#18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print((7//3) == (int(2.7)))

#19 - Check if type of '10' is equal to type of 10
print(type('10')== type(10))

# 20 - Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# 21 - Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours=(int(input("please enter your hours worked ")))
rate=(float(input("please enter your rate ")))
print("Your wages are ", (rate * hours))

# 22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Years_lived=int(input("Enter number of years you have lived: " ))
print("You have lived for ", (Years_lived * 365 * 24 * 60 * 60), "seconds")

# 23 - Write a Python script that displays the following table
for i in range (1,6):
    print(i*1,i,i*1,i**2,i**3)
