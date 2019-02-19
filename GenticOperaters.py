import random
from ExpressionAndParser import CNFSatisfiablityExpression
from ExpressionAndParser import Parser
def mutate(rate,inputstring):
    mutated_string =  ""
    r = random.random()
    for i in inputstring:
        if r < rate:
            if i =='1':
                mutated_string += '0'
            else:
                mutated_string += '1'
        if r > rate:
            if i == '0':
                mutated_string += '1'
            else:
                mutated_string += '0'

    return mutated_string
def crossover(string1, string2, pivot):
    string1 = cross_over_string_1
    string2 = cross_over_string_2
    newstring1 = []
    newstring2 = []
    i=0
    h=0
    for l in string2:
        newstring1.append(string1[l])
        i+=1
        if i == pivot:
            break
    for x in range(pivot, len(string2)):
        newstring1.append(string2[x])
    
    for j in string1:
        newstring2.append(string2[j])
        h+=1
        if h == pivot:
            break
    for k in range(pivot, len(string1)):
        newstring2.append(string1[k])
    return newstring1,newstring2

def genpopulation(string, size):
    for i in range(0, size):
        values = []
    for j in string:
        values.append(random.randint(0,1))
    return values

l1=[]
parserlist_a =[]
parserlist_b =[]

#1st test case for mutate a string of all 0s should be returned as the value of result1_actual.
result1_actual = mutate(1,"111111")
result1_expected = "000000"
if(result1_actual == result1_expected):
    print ('passed mutate test1')
#2nd test case for mutate a string of all 1s should be returned as the value of result1_actual.
result2_actual = mutate(1,"000000")
result2_expected = "111111"
if(result2_actual == result2_expected):
    print ('passed mutate test2')

#strings for crossover function.
cross_over_string_1 = [1,1,0,0,0,1]
cross_over_string_2 = [1,1,1,0,0,0]

#test case 1 for crossover a string of numbers in this order (112111) should be returned as the value of st1.
#test case 2 for crossover a string of numbers in this order (221000) should be returned as the value of st2.
result3_actual = crossover(cross_over_string_1,cross_over_string_2,3)
result3_expected = [1,1,1,0,0,0],[1,1,1,0,0,1]
if(result3_actual == result3_expected):
    print("passed crossover test")

newpop = genpopulation(cross_over_string_1,len(cross_over_string_1))
