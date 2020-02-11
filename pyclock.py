from datetime import datetime
from time import sleep
from sys import stdout
import winsound
from multiprocessing import Process

# Global Variables
app_running = True
frequency = 150
task_time = 0
break_time = 0

# Creates a clock that runs in place.
# Note that this clock runs depending on your system time
def clock():
    while app_running:

        sleep(1)
        time = datetime.now().strftime('%H:%M:%S')

        stdout.write('\r%s' % time)
        stdout.flush()
    stdout.write('\n')
# clock()

def user_time():
    global task_time, break_time

    task_time = int(input('Enter for how many minutes do you want to perform the task.\n'))
    break_time = int(input('Enter how long will be your breaks (5 minutes is good practice.)\n'))

    return task_time, break_time

def pomodoro_timer(task_time, break_time):
    while app_running:
        sleep(task_time)
        print(f'\n\nTime to work!'
              f'\nTry to focus on your task for {task_time} minutes.'
              f'\nYour computer will sound when is time to take a break.')
        winsound.MessageBeep(frequency)

        sleep(break_time)
        print(f'\n\nIt is break time!'
              f'\nYou have {break_time} minutes to do something not related to the task.'
              f'\nYour computer will make a sound when the break is over.')
        winsound.MessageBeep(frequency)
# pomodoro_timer()

if __name__ == '__main__':
    Process(target=pomodoro_timer, args=(user_time())).start()
    Process(target=clock).start()