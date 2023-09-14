end = []
long_list = []
number_of_test_cases = int(input())

def looper(tester_case):

    if tester_case[0]*3 >= tester_case[1]:
        return tester_case[0] , tester_case[0] * 3

    tester_case[0] = tester_case[1] // 3

    while True:
        if tester_case[0]*3 >= tester_case[1]:
            return tester_case[0] , tester_case[0] * 3

        tester_case[0] = tester_case[0] + 1

for a in range(0,number_of_test_cases):
    test_case = input().split(' ')
    test_case[0] , test_case[1] = int(test_case[0]) , int(test_case[1])
    long_list.append(test_case)

for each_test_case in long_list:
    tmp = []
    tmp.extend(each_test_case)

    right_answer = looper(each_test_case)
    end.append(( right_answer[0] - int(tmp[0]) ) + ( right_answer[1] - int(tmp[1]) ))

for a in end:
    print (a)

