import datetime
import time
import winsound  # For Windows sound

while True:
    
    print("Current Date and Time:", datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    # Every 5 seconds, play a beep sound

    if int(datetime.datetime.now().strftime("%S")) % 5 == 0:  # Display current time

        winsound.Beep(1000, 500)  # frequency=1000Hz, duration=500ms

    time.sleep(1)  # Wait for 1 second

