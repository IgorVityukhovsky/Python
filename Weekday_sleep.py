# pip install keyboard pywin32

import datetime
import keyboard
import os
import time
import win32api

def is_working_hours():
    now = datetime.datetime.now()
    weekday = now.weekday()
    start_time = datetime.datetime(now.year, now.month, now.day, 9, 0)

    if weekday < 4:
        end_time = datetime.datetime(now.year, now.month, now.day, 18, 15)
    else:
        end_time = datetime.datetime(now.year, now.month, now.day, 17, 0)

    return start_time <= now <= end_time

def prevent_sleep():
    keyboard.press_and_release('f15')

def hibernate():
    os.system("shutdown /h")

def check_user_activity(timeout):
    last_activity = time.time()

    while True:
        user_idle_time = (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000
        print(user_idle_time)

        if user_idle_time >= timeout:
            return True
        

        if user_idle_time < timeout:
            print("sleep time, wait")
            time.sleep(30)

def main():
    timeout = 300 # 300 секунд (5 минут) бездействия пользователя

    while True:
        if is_working_hours():
            prevent_sleep()
            print("Dont sleep")
            

        else:
            if check_user_activity(timeout):
                hibernate()

        time.sleep(60)  # Проверяем состояние каждую минуту

if __name__ == '__main__':
    main()
