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


def common_elements(list1, list2):
    temp=[]

    for element in list1:
        if element in list2:
            temp.append(element)
    return temp
    #print (temp[])
#maybe
#def common_elements(list1, list2): return [element for element in list1 if element in list2]

a=[1,2,3,4,5,645,74,99,22,1997,42,69,96]
b=[1,2,3,4,5,72,23,754,100,1997,46,58,196]
common_elements(a,b)