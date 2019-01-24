import math
#1-15-19
#Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
#The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!
#def
# variable1= raw_input("")
# variable2= raw_input("")
# variable3= raw_input("")

#2.

#Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#extras:

#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#List pro


#def common_elements(list1, list2):
#   temp=[]
#  for element in list1:
#     if element in list2:
    #        temp.append(element)
    #return temp
    #print (temp[])
#maybe
#def common_elements(list1, list2): return [element for element in list1 if element in list2]

#a=[1,2,3,4,5,645,74,99,22,1997,42,69,96]
#b=[1,2,3,4,5,72,23,754,100,1997,46,58,196]
#common_elements(a,b)



#1-17-19

#Create a function that will take as input a list of numbers.
#it will output a bitstring in binary that will.
#represent whether the element in the list was even or odd.
#def Create_List (listA[]):
#    for listA.output.bitstring.binary()
#
#      if listA.element.returns.odd.numbers
#       print ("Odd numbers returned")

#        if listA.element.returns.even.numbers
 #       print("Even numbers returned")


#Create a function that will determine if the input value is even or odd. return 1 for odd 0 for even
#def oddOReven(input_number):
#  if input_number = even.number
#       print("even number was entered")
# if input_number.returns.odd.number
#    print("odd number was entered")


#1-24-19

#Morning problem: Create a function.
#arguments: number of slices and radius.
#returns: a list of tuples .
#Description: returns a list of (,) with respect to the unit circle given number of slices and radiuse.
#estimated time to complete: 30 m.
def function(slices,radius)
    points = []
    _angle = 0
    for slice in range(slices):
        _angle +=slice/(1*math.pi)
        circle=(radius * math.cos(angle),raduis * math.sin(angle)
        return points

