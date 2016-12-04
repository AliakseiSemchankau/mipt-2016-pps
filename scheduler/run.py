from flask import Flask, request, abort
# from order_scheduler_pb2 import *
# from computing_system_scheduler_pb2 import *
from json import loads
from sys import argv
from uuid import uuid4 as uuid
import requests
app = Flask(__name__)

import pickle
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import order_scheduler
from order_scheduler import Order

ALGORITHM_ADDRESS=''
ORDER_ADDRESS=''
SYSTEM_ADDRESS=''
SCHEDULER_ADDRESS=''

@app.route("/add_task", methods=['POST'])
def addTask():
    order_id = str(uuid())
    order = pickle.loads(request.get_data())
    order.order_id = order_id
    resp = requests.post(ALGORITHM_ADDRESS + '/add_task', data=order.SerializeToString())
    if not resp.ok:
        abort(res.code)
    return order_id

@app.route("/get/<order_id>")
def getResult(order_id):
    resp = requests.post(SYSTEM_ADDRESS + '/get/' + order_id)
    if not resp.ok:
        abort(res.code)
    return resp.content

@app.route('/send_subtask', methods=['POST'])
def sendSubTask():
    resp = requests.post(SYSTEM_ADDRESS + '/send_subtask', data=request.get_data())
    if not resp.ok:
        abort(res.code)
    return resp.content

@app.route('/info')
def getInfo():
    resp  = requests.get(SYSTEM_ADDRESS + '/info')
    return resp.content

@app.route('/notify', methods=['POST'])
def onSubTaskCompletion():
    resp = requests.post(ALGORITHM_ADDRESS + '/send_subtask', data=request.get_data())
    if not resp.ok:
        abort(res.code)
    return resp.content

if __name__ == '__main__':
    conf = loads(open(argv[1]).read())
    ALGORITHM_ADDRESS = 'http://' + conf['algorithm_address']
    ORDER_ADDRESS = 'http://' + conf['order_address']
    SYSTEM_ADDRESS = 'http://' + conf['system_address']
    SCHEDULER_ADDRESS = conf['scheduler_address']
    addr = SCHEDULER_ADDRESS.split(':')
    conf = {'host': addr[0]}
    if len(addr) > 1:
        conf['port'] = addr[1]
    app.run(**conf)
