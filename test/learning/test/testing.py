from random import randint
import time

def QNA ():

    while True:

        first_number = randint(1 , 25)
        second_number = randint(25 , 50)

        start_timer = time.time()
        player_answer = input('%i * %i = ' % (first_number , second_number))
        correct_answer = first_number*second_number

        if player_answer == 'out':
            break

        print()
        print(time.time() - start_timer)
        if int(player_answer) == correct_answer:
            print('Correct')

        else:
            print('Wrong')
            print('correcr answer is %i' % correct_answer)

QNA()

