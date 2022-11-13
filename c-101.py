import time
# print(dir(time))
# print(time.localtime)

seconds=input("Enter The Time in Number of Seconds: ")
def countDownTimer(seconds):
    while seconds>0:

        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}: {secs}'
        print(timer)
        time.sleep(1)
        seconds = seconds-1
    print("Time up!")

countDownTimer(int(seconds))