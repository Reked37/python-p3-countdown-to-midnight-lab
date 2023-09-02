# your code goes here!
import time
def countdown(timer):
    while timer<10:
        print(f'{timer} SECOND(S)!')
        timer -=1
        if timer == 0:
            return print('HAPPY NEW YEAR!')

def countdown_with_sleep(timer):
    while timer <10:
        print(f'{timer} SECOND(S)!')
        time.sleep(1)
        timer -=1
        if timer == 0:
            return print('HAPPY NEW YEAR!')