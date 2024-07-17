from datetime import datetime
from playsound import playsound
alarm_time = input("enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_seconds=alarm_time[9:11].upper()
print("setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_minute = now.strftime("%S")
    current_period = now.strftime("%P")
    if(alarm_hour==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("wake up!")
                    playsound('audio.mp3')
                    break