first_input = input().split(' ')
second_input = input().split(' ')
int_second_input = []
counter_answer = 0
counter_looper = 0

def looper(int_second_input):
    global counter_answer
    global counter_looper

    for number_each_color in range(0 , int(first_input[0])):
        if int_second_input[number_each_color]//2 + sum(int_second_input) - int_second_input[number_each_color] <= int(first_input[1]):
            (int_second_input[number_each_color])
            return counter_answer + 1

    int_second_input[counter_looper] = int_second_input[counter_looper]//2
    counter_answer += 1
    counter_looper += 1

    if counter_looper == len(int_second_input):
        counter_looper = 0

    return looper(int_second_input)

def Run():

    for each_number in second_input:
        int_second_input.append(int(each_number))

    if int (first_input[1]) == 0:
        return (first_input[0])

    return looper(int_second_input)

print(Run())
