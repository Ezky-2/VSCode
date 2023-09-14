from math import factorial as factorial
# a = (factorial(30 + 30 - 2)//factorial(30-1)) - ((factorial(15 + 15 -2)//factorial(15-1))  + (factorial(30 + 30 - 15 -15)//factorial(30 - 15)))
# print(a)

def factorial_calc (first_variable , second_variable , third_variable , fourth_variable):
    upper_case = factorial(first_variable + second_variable - third_variable - fourth_variable)
    first_downer_case = factorial(first_variable - third_variable)
    second_downer_case = factorial(second_variable - fourth_variable)

    return upper_case // (first_downer_case * second_downer_case)

x = list(map(int , input().split(' ')))

a = factorial_calc(x[0] , x[1] , 1    , 1   )
b = factorial_calc(x[2] , x[3] , 1    , 1   )
c = factorial_calc(x[0] , x[1] , x[2] , x[3])

print(a - (b * c))