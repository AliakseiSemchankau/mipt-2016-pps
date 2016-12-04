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


@app.route("/add_task", methods=['POST'])
def addTask():
    order = Order()
    order.ParseFromString(request.get_data())
    pending_orders.append(order)
    return order.order_id


def sendTasks():
    while True:
        try:
            while len(pending_orders) == 0:
                time.sleep(random.randint(1, 2))
            order = pending_orders.pop()
            order_id = order.order_id
            sub_tasks = order.task.sub_tasks
            cluster_id = random.randint(1, 10)
            for sub_task in sub_tasks:
                sub_task_order = SubTaskOrder()
                sub_task_order.order_id = order_id
                sub_task_order.sub_task.CopyFrom(sub_task)
                sub_task_order.cluster_id = cluster_id
                resp = requests.post(SCHEDULER_ADDRESS + '/send_subtask', data=sub_task_order.SerializeToString())
            return resp.content
        except Exception as e:
            print(e)


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
    app.run(**conf)
