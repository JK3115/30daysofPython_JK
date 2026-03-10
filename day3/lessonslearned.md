# Lessons learned
1. During one of the exercises, I could not get a print function to work for this code 
   
    >print(2 == slope)

The error code was  
    >print(2 == slope)
    > ~~~~~^^^^^^^^^^^^
    >TypeError: 'str' object is not callable

I could not understand at all what was causing it for longer than I'd care to admit. After stepping away and coming back. I realized the error. The line of code had a pretty critical mistake. 

   >print=(f"The

I had accidentally assigned the print function to something else entirely and it no longer functioned. Reassigning a builtin function would cause considerable problems. This was a good one to learn.

2. I also experienced an error while attempting to perform a mathematical caluclation.

   >print("You have lived for ", (Years_lived * 365 * 24 * 60 * 60), "seconds")

This line of code kept generating repeating numbers for the user input. I could understand why. I tried several iterations that shouldhave worked. After looking at the code preceding it...

   >Years_lived=(input("Enter number of years you have lived: " ))

I realized (after reviewing other sections from operators.py), I had failed to define the type of input (int). 
        
   >Years_lived=int(input("Enter number of years you have lived: " ))
   
Once I declared it, the script worked exactly as I expected.

3. Some of the solutions worked with for loops that I had previously been familiar with but didn't completely feel comfortable with. For example:
" 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0."

    >for x in range (-10,10):
    >y=((x**2)+6*x+9)
    >if y== 0:
        print("Y is 0 when X is ", x)
        break # Solution is Y is 0 when x = -3
    >else:
        print("X value is not in range")

This utilized a for loop to cycle through a range of solutions and comparison logic to solve a problem. This really helped me to understand how to use for ,if, else, and break in the future. 
