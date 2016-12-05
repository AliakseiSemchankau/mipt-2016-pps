from flask import Flask, request, abort
from messages.order_scheduler_pb2 import *
from messages.computing_system_scheduler_pb2 import *
from json import loads
from sys import argv
from uuid import uuid4 as uuid
import requests
app = Flask(__name__)

ALGORITHM_ADDRESS=''
ORDER_ADDRESS=''
SYSTEM_ADDRESS=''
SCHEDULER_ADDRESS=''

@app.route("/add_task", methods=['POST'])
def addTask():
    order_id = str(uuid())
    order = Order()
    order.ParseFromString(request.get_data())
    order.order_id = order_id
    resp = requests.post(ALGORITHM_ADDRESS + '/add_task', data=order.SerializeToString())
    if not resp.ok:
        abort(resp.status_code)
    return order_id

@app.route("/get/<order_id>")
def getResult(order_id):
    resp = requests.get(SYSTEM_ADDRESS + '/get/' + order_id)
    if not resp.ok:
        abort(resp.status_code)
    return resp.content

@app.route('/send_subtask', methods=['POST'])
def sendSubTask():
    resp = requests.post(SYSTEM_ADDRESS + '/send_subtask', data=request.get_data())
    if not resp.ok:
        abort(resp.status_code)
    return resp.content

@app.route('/info')
def getInfo():
    resp  = requests.get(SYSTEM_ADDRESS + '/info')
    if not resp.ok:
        abort(resp.status_code)
    return resp.content

@app.route('/notify', methods=['POST'])
def onSubTaskCompletion():
    resp = requests.post(ALGORITHM_ADDRESS + '/notify', data=request.get_data())
    print('notify ' + ALGORITHM_ADDRESS + '/notify')
    if not resp.ok:
        abort(res.status_code)
    return resp.content

if __name__ == '__main__':
    conf = loads(open(argv[1]).read())
    ALGORITHM_ADDRESS = 'http://' + conf['algorithm_address']
    SYSTEM_ADDRESS = 'http://' + conf['system_address']

    addr = conf['scheduler_address'].split(':')
    conf = {'host': addr[0]}
    if len(addr) > 1:
        conf['port'] = addr[1]
    app.run(**conf)
