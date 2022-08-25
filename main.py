import requests
import threading
import time
session = requests.Session()

time.sleep(2)
webhook = input("enter webhook url: ")
message = input("enter the message to send: ")
username = input("enter the webhook's username: ")
def hook():
    session.post(webhook,json = {"content":message,"username":username})
    
    while True:
        for i in range(15):
            threading.Thread(target=hook).start()
hook()

for i in range(15):
    threading.Thread(target=hook).start()
hook()
