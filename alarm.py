import time
from playsound import playsound

def alarm_clock(alarm_time, sound_file):
    print(f"Alarm set for {alarm_time}. Waiting...")

    while True:
        # Get current time in HH:MM format
        now = time.strftime("%H:%M")

        if now == alarm_time:
            print("Wake up!")
            playsound(sound_file)
            break
        time.sleep(10)  # check every 10 seconds to save CPU

if __name__ == "__main__":
    alarm_time = input("Set alarm time (HH:MM in 24-hour format): ")
    sound_file = "alarm.mp3"  # replace with path to your sound file

    alarm_clock(alarm_time, sound_file)
