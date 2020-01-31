
'''Question

Write a program to calculate area of shapes. Your program should be capable of calculating the area of a square, rectangle, triangle and 
a circle. The user should be presented with options to select the shape. Based on which shape is chosed by the user, the program should 
ask for the appropriate input and print the resulting area on the screen. When the program is run, the screen should display something 
like this:

Which shape would you like to calculate the area for? Please enter the option number-

Square
Rectangle
Triangle
Circle Enter Option: _
Say the user enters the option 1.

Please enter the length of a side: _

If the user enters a value of 5. The output should be:

The area of the square is 25

This program should indicate that the input is invalid if the user enters a character instead of a number as input. For instance if the user enters a value of ‘a’ instead of 5 in the previous example the program should prompt:

Invalid input, please enter a number: _ '''


i=int(input('''
Which shape would you like to calculate the area for? Please enter the option number- 
1. Square 
2. Rectangle 
3. Triangle 
4. Circle 
Enter Option: _
'''))

def square():
    a=(input("enter the length of a side:_ "))
    if a.isdigit()==True:
        b=int(a)
        c=b*b
        print("The area of the square is: ",c)
        return c
    else:
        print("Invalid input, please enter a number")
        print()
        square()

def rect():
    l=(input('enter the length of rectangle:_ '))
    br=(input("enter the breadth of the rectangle:_ "))
    if l.isdigit() and br.isdigit()==True:
        length=int(l);breadth=int(br)
        n=length*breadth
        print("The area of the Rectangle is: ",n)
        return n
    else:
        print("Invalid input, please enter a number")
        print()
        rect()

def triangle():
    h=(input("enter the height of the triangle:_ "))
    b1=(input("enter the base of the triangle:_ "))
    if h.isdigit() and b1.isdigit()==True:
        height=int(h);base=int(b1)
        n1=(height*base)/2
        print("The area of the Triangle is: ",n1)
        return n1
    else:
        print("Invalid input, please enter a number")
        print()
        triangle()
    

def circle():
    r=(input("enter the radius of the circle:_ "))
    if r.isdigit()==True:
        radius=int(r)
        n2=3.14*radius**2
        print("The area of the circle is: ",n2)
        return n2
    else:
        print("Invalid input, please enter a number")
        print()
        circle()
    
if i==1:
    square()
elif i==2:
        rect()
elif i==3:
        triangle()
elif i==4:
    circle()
else:
    print("Invalid option")
