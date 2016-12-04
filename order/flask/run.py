#!flask/bin/python
from json import loads
from sys import argv
from flask import Flask, request, abort
from flask import render_template, flash, redirect
from order_scheduler_pb2 import *
from computing_system_scheduler_pb2 import *
import requests

from app import app

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required

class OrderForm(Form):
    sub_tasks_urls = TextField('sub_tasks_urls', validators=[Required()])
    processors_count = IntegerField('processors_count', validators=[Required()])
    time_durability = IntegerField('time_durability', validators=[Required()])

def send_order(subtasks_urls, processors_count, time_durability):
    task = Task()
    for url in subtasks_urls:
        sub_task = task.sub_tasks.add()
        sub_task.url = url
    order = Order()
    order.task.CopyFrom(task)
    order.resource.processors_count = processors_count
    order.resource.time_durability = time_durability
  
    resp = requests.post(SCHEDULER_ADDRESS + '/add_task', data=order.SerializeToString())
    if not resp.ok:
       
        abort(resp.status_code)

    return resp.content

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():

    order_form = OrderForm()

    kwargs = {'order_form': order_form}

    if order_form.validate_on_submit():

        sub_tasks_urls = str(order_form.sub_tasks_urls.data).split(' ')
        processors_count = int(order_form.processors_count.data)
        time_durability = int(order_form.time_durability.data)

        order_id = send_order(sub_tasks_urls, processors_count, time_durability)

        kwargs['order_id'] = order_id

        return render_template("index.html", **kwargs)

    return render_template("index.html", **kwargs)



if __name__ == '__main__':
	conf = loads(open(argv[1]).read())

	SCHEDULER_ADDRESS = 'http://' + conf['scheduler_address']

	addr = conf['order_address'].split(':')
	conf = {'host': addr[0]}
	if len(addr) > 1:
	    conf['port'] = addr[1]
	conf['debug']=True

	app.run(conf['host'], int(conf['port']), debug=True)