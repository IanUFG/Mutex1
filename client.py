
from flask import Flask
import json
from flask import request
import sys
import const 
import requests
import threading
# Handle interactive loop


def consult():
    response = requests.get(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/get')
    response   = json.loads(response.text)
    print('The current value is '+str(response['count'])+'\n\n')

def increment():
    value = input("Value to be incremented: \n")
    data = {
        'value' : value
    }
    response = requests.post(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/increment', json = data) 

    response   = json.loads(response.text)
    print('Count incremented by ' + str(value) + ' - Total = '+ str(response['count']))
def run():
    while True:
        
        reply = input("1- Consult\n2- Increment\n")
        if(reply == '1'):
            consult()
        elif (reply == '2'):
            consult()
            increment()
        else:
            print('Invalid option! \n')
        


if __name__ == '__main__':
    run()