
from flask import Flask
from flask import jsonify
from flask import request
import const 
import requests

app = Flask(__name__)

print("Chat Server is ready...")

count = 0


@app.route('/get',methods=['GET'])
def consult():
    global count
    print('the actual value is ' + str(count))
    return {'count':count}


@app.route('/increment',methods=['POST'])
def increment():
    global count
    current = count

    count += int(request.json['value'])

    print('Count ' + str(current) + ' incremented by ' + str(request.json['value']) + ' - Total = '+ str(count))

    return {'count':count}

if __name__ == '__main__':
    app.run(host=const.CHAT_SERVER_HOST, port=const.CHAT_SERVER_PORT, debug=True)