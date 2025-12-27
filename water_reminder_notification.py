import time 
from plyer import notification

while True :
    notification.notify(title = 'Drink water' , message = 'Have a glass of water')
    time.sleep(60*60)
    print("successful")