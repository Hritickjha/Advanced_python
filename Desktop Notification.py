import time
from pyclbr import notification

if_name_ == "_main_":    
while True:
        notification.notify(
            title ="ALERT!!!",
            message = "Take a break! IT has been an hour!",
            timeout =10
        )
        time.sleep(3600)