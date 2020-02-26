from datetime import datetime, timedelta
from time import sleep
from sys import stdout
import winsound
from multiprocessing import Process

# Global Variables
app_running = True
frequency = 150
task_time = 0
break_time = 0
time_in_seconds = 0
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

def convert_to_seconds(number_to_convert):
    # Grab any amount of time and converts to seconds
    global time_in_seconds

    time_in_seconds = number_to_convert * 60

def user_time():
    global task_time, break_time

    task_time = int(input('Enter for how many minutes do you want to perform the task.\n'))
    break_time = int(input('Enter how long will be your breaks (5 minutes is the usual.)\n'))

    return task_time, break_time

def pomodoro_timer(t_time, b_time):
    while app_running:
        sleep(t_time)
        print(f'\n\nTime to work!'
              f'\nTry to focus on your task for {t_time} minutes.'
              f'\nYour computer will sound when is time to take a break.')
        winsound.MessageBeep(frequency)

        sleep(b_time)
        print(f'\n\nIt is break time!'
              f'\nYou have {b_time} minutes to do something not related to the task.'
              f'\nYour computer will make a sound when the break is over.')
        winsound.MessageBeep(frequency)
# pomodoro_timer()


def timer():
    # User timer that when it reaches 0 it will make a sound
    time_lapse = int(input("Enter the amount of minutes you would like for your count down."))

    for num in reversed(range(time_lapse*60+1)):
        sleep(1)
        print(num)
# timer()

def go_to_bed():
    # At what time does the user want to go to bed
    rest_time = int(input('How many hours would you like to sleep.'))
    sleep(rest_time*3600)
    winsound.PlaySound()

# go_to_bed()

def alarm():
    # At what time does the user want to go to bed
    rest_time = int(input('How many hours would you like to sleep.'))
    sleep(rest_time*3600)
    winsound.PlaySound()

# alarm()

if __name__ == '__main__':
    Process(target=pomodoro_timer, args=(user_time())).start()
    Process(target=clock).start()