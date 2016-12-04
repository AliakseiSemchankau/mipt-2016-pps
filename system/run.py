from flask import Flask, request, abort
from order_scheduler_pb2 import *
from computing_system_scheduler import *
from json import loads
from sys import argv
import threading
import requests
import time
app = Flask(__name__)

SYSTEM_ADDRESS=''
SCHEDULER_ADDRESS=''

tasks_to_execute = []
results = {}

have_tasks = threading.Condition()

@app.route("/get/<order_id>")
def getResult(order_id):
    if order_id in results:
        msg = StatusMsg()
        if results[order_id] is None:
            msg.status = StatusMsg.StatusType.UNDONE
        else:
            msg.status = StatusMsg.StatusType.DONE
            msg.result = results[order_id]
        return msg.SerializeToString()
    else:
        abort(401)

@app.route('/send_subtask', methods=['POST'])
def sendSubTask():
    order = SubTaskOrder()
    order.ParseFromString(request.get_data())

    have_tasks.acquire()
    tasks_to_execute.append(order)
    results[order.order_id] = None
    have_tasks.notify()
    have_tasks.release()

@app.route('/info')
def getInfo():
    msg = ClusterSystemMsg()
    for i in range(10):
        cluster = msg.clusters.add()
        for j in range(5+i%2):
            processor_msg = cluster.processors.add()
            processor_msg.power = i%3 + j%2 + 1
            processor_msg.reserved_time = 0
    return msg.SerializeToString()

def ComputeResults():
    while True:
        have_tasks.acquire()
        task = None
        while len(tasks_to_execute) == 0:
            task = tasks_to_execute.pop()
        have_tasks.release()

        #stub for computing task
        print('computing: ' + task.sub_task.url)
        time.sleep(rand.randint(2, 4))
        results[task.order_id] = str(rand.randint(20))

        msg = StatusMsg()
        msg.status = StatusMsg.StatusType.DONE
        try:
            requests.put(SCHEDULER_ADDRESS + '/notify', data=msg.SerializeToString())
        except Exception as e:
            print(e)


if __name__ == '__main__':
    conf = loads(open(argv[1]).read())
    SCHEDULER_ADDRESS = 'http://' + conf['scheduler_address']
    addr = conf['system_address'].split(':')
    conf = {'host': addr[0]}
    if len(addr) > 1:
        conf['port'] = addr[1]
    t = threading.Thread(target=ComputeResults)
    t.setDaemon(True)
    t.start()
    app.run(**conf)
