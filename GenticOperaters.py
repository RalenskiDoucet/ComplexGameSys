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
    ran_list = [1,1,1,1,1,1,1,1,1,1]
    newstring = []
    i=0
    for l in newstring:
        if i == pivot:
            for x in range(pivot, string2.__len__()):
                newstring.append(string2[x])
            return newstring
        else:
            i+=1

l1=[]
parserlist_a =[]
parserlist_b =[]
cross_over_string_1 = []
cross_over_string_2 = []

#1st test case for mutate a string of all 0s should be returned as the value of result1_actual.
result1_actual = mutate(1,"111111")
result1_expected = "000000"
if(result1_actual == result1_expected):
    print ('pass test1')
#2nd test case for mutate a string of all 1s should be returned as the value of result1_actual.
result2_actual = mutate(1,"000000")
result2_expected = "111111"
if(result2_actual == result2_expected):
    print ('pass test2')

#strings for crossover function.
cross_over_string_1 = "110001"
cross_over_string_2 = "221000"

#test case 1 for crossover a string of numbers in this order (112111) should be returned as the value of st1.
#test case 2 for crossover a string of numbers in this order (221000) should be returned as the value of st2.
crossover(cross_over_string_1,cross_over_string_2,3)

