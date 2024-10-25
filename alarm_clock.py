from playsound import playsound
#playsound('Personal/Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3')
import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
       
        time_left = seconds - time_elapsed
        days_passed = time_left // 86400
        hours_passed = (time_left % 86400) // 3600
        seconds_passed = time_left % 60
        minutes_passed = (time_left % 3600) // 60
        print(f"{CLEAR_AND_RETURN}An alarm will sound after:{days_passed:02d}:{hours_passed:02d}:{minutes_passed:02d}:{seconds_passed:02d}")

    playsound('Personal/Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3')


days = int(input(f"How many days do you want: "))
hours = int(input(f"How many hours do you want: "))
minutes = int(input(f"How many minutes do you want: "))
seconds = int(input(f"How many seconds do you want: "))
total_time = days * 86400 + hours * 3600 + minutes * 60 + seconds


alarm(total_time)