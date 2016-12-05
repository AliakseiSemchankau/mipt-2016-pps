from flask import Flask, request, abort
from order_scheduler_pb2 import *
from computing_system_scheduler_pb2 import *
import sys
from json import loads
from sys import argv
import threading
import random
import time
from uuid import uuid4 as uuid
import requests
app = Flask(__name__)

ALGORITHM_ADDRESS=''
SCHEDULER_ADDRESS=''

pending_orders = []
pending_sub_tasks = []


@app.route("/add_task", methods=['POST'])
def addTask():
    order = Order()
    order.ParseFromString(request.get_data())
    pending_orders.append(order)
    return order.order_id


def sendTasks(sub_task_id=""):
    global pending_sub_tasks
    while True:
        try:
            if len(pending_sub_tasks) != 0:
                sub_task = pending_sub_tasks.pop()
                cluster_id = random.randint(1, 10)
                sub_task_order = SubTaskOrder()
                sub_task_order.order_id = sub_task_id
                sub_task_order.sub_task.CopyFrom(sub_task)
                sub_task_order.cluster_id = cluster_id
                resp = requests.post(SCHEDULER_ADDRESS + '/send_subtask', data=sub_task_order.SerializeToString())
                exit_status = resp.content
                print("Send subtask " + str(sub_task_order))
                return exit_status
            elif len(pending_orders) != 0:
                order = pending_orders.pop()
                order_id = order.order_id
                sub_tasks = list(order.task.sub_tasks)
                sub_task = sub_tasks.pop()
                pending_sub_tasks += sub_tasks
                cluster_id = random.randint(1, 10)
                sub_task_order = SubTaskOrder()
                sub_task_order.order_id = order_id
                sub_task_order.sub_task.CopyFrom(sub_task)
                sub_task_order.cluster_id = cluster_id
                resp = requests.post(SCHEDULER_ADDRESS + '/send_subtask', data=sub_task_order.SerializeToString())
                exit_status = resp.content
                print("Send subtask " + str(sub_task_order))
                return exit_status
        except Exception as e:
            print(e)


@app.route('/notify', methods=['POST'])
def onSubTaskCompletion():
    status_msg = StatusMsg()
    status_msg.ParseFromString(request.get_data())
    t = threading.Thread(target=sendTasks, args=(status_msg.order_id,))
    t.daemon = True
    t.start()
    return ""

if __name__ == '__main__':
    conf = loads(open(argv[1]).read())
    SCHEDULER_ADDRESS = 'http://' + conf['scheduler_address']
    addr = conf['algorithm_address'].split(':')
    conf = {'host': addr[0]}
    if len(addr) > 1:
        conf['port'] = addr[1]
    t = threading.Thread(target=sendTasks)
    t.daemon = True
    t.start()
    order = Order()
    pending_orders.append(order)
    app.run(**conf)
