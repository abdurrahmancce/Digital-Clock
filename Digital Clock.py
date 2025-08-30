import datetime
import time
import winsound 

while True:
    
    print("Current Date and Time:", datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))


    if int(datetime.datetime.now().strftime("%S")) % 5 == 0:  

        winsound.Beep(1000, 500) 

    time.sleep(1) 


