#Python Application Code
#CREATED BY AIDAN CARRIER 
#11/18/2020
#For use for the Bucs Robotics Club teaching event(s)

#Python Tutorial:

#What is Python?
#Python is an object oriented programming language...

#variables:
#a variable stores a value

#data types:

#integers
exampleInteger = 3

#floats, doubles
exampleFloat = 3.0043
exampleDouble = 2.50

#chars
exampleChar = 'a'

#strings 
exampleString = "this is a string"

#booleans (True or False) CAP SENSITIVE!!!
exampleBool = True

#print statement:
print("hello world!") #prints to console / terminal

#operators
a = 1
b = 2

#addition (+) -- adds the two terms
c = a + b   #this will give c a value of 3
print(c)    #print value of variable c to console

#subtraction (-) -- subracts the second term from first term
c = a - b
print(c)

#multiplication (*) -- gives the product of the two terms
c = a * b
print(c)

#division (/) -- gives the quotient (not including the remainer)
c = a / b
print(c)

#modulus (%) -- gives the remainder
c = a % b
print(c)

#functions/methods

#in Python, functions are defined using 'def'

def myFunction (parameter): #the parameters (optional) are elements used in the function when called
    print("this number is ", parameter)
    return #ended with a return statement

#calling the function:
myFunction(c)
myFunction('nonexistant')

#Arrays
myArray = ["a", "b", "c"]
print(myArray[0])

#Loops:

#while loop
iteration = 0
while(iteration < 3):
    print(myArray[iteration])
    iteration += 1

#for (each) loops
for element in myArray:
    print(element)

#Classes
class MyClass:
    'a class descriptor goes here'

    #class variables
    variableInClass = False

    #constructor
    def __init__(self, parameters):
        self.parameters = parameters

    #methods in class
    def functionInClass(self):
        print("woo!", self.parameters)
        return

#class objects
thisClass = MyClass("yay")

#getting a value in class:
print(thisClass.variableInClass)

#calling a function in class
thisClass.functionInClass()
    