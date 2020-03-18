import subprocess
import platform
from time import sleep


# i = 0
# for idx, i in enumerate(range(0, 9)):
#     if idx <= 4:
#         print(f"\r{str(i)*20}")
#     else:
#     time.sleep(1)





def clear_screen():
    # thanks to: https://stackoverflow.com/a/23075152/2923937
    if platform.system() == "Windows":
        subprocess.Popen("cls", shell=True).communicate()
    else:
        print("\033c", end="")


# obviously you can create a function to convert your string into this
# list rather than doing it manually like I did, but that is another question :p.
views = ['#\nh\n#', '##\nhe\n##', '###\nhel\n###', '####\nhell\n####', '#####\nhello\n#####']



for view in views:
    clear_screen()
    print(view)
    sleep(0.5)

