#!flask/bin/python
from json import loads
from sys import argv
from flask import Flask, request, abort
from flask import render_template, flash, redirect
from messages.order_scheduler_pb2 import *
from messages.computing_system_scheduler_pb2 import *
import requests

from order.flask.app import app

from flask_wtf import Form
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required

import sqlite3

class OrderForm(Form):
    user_login = TextField('user_login', validators=[Required()])
    sub_tasks_urls = TextField('sub_tasks_urls', validators=[Required()])
    processors_count = IntegerField('processors_count', validators=[Required()])
    time_durability = IntegerField('time_durability', validators=[Required()])

class ResultForm(Form):
	user_login = TextField('user_login', validators=[Required()])
	order_id = TextField('order_id', validators=[Required()])

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

def get_result(order_id):

	resp = requests.get(SCHEDULER_ADDRESS + '/get/' + order_id)
	result = StatusMsg()
	result.ParseFromString(resp.content)

	return result


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():

    order_form = OrderForm()
    result_form = ResultForm()

    conn = sqlite3.connect('test.db')

    kwargs = {'order_form': order_form, 'result_form': result_form}

    if order_form.validate_on_submit():
        user_login = str(order_form.user_login.data)
        sub_tasks_urls = str(order_form.sub_tasks_urls.data).split(' ')
        processors_count = int(order_form.processors_count.data)
        time_durability = int(order_form.time_durability.data)

        print ("SELECT money FROM user_money WHERE user = {}".format(user_login))

        cursor = conn.execute("SELECT money FROM user_money WHERE user = '{}'".format(user_login))
        for row in cursor:
            money = row[0]

        cost = processors_count * time_durability

        try:
            if money < cost:
                kwargs['money'] = money
                kwargs['rejected'] = True
                conn.close()
                return render_template("index.html", **kwargs)
        except Exception:
            kwargs['money'] = 'CANT GET MONEY AMOUNT FOR THIS USER'
            kwargs['rejected'] = True
            conn.close()
            return render_template("index.html", **kwargs)
         
        money -= cost

        order_id = send_order(sub_tasks_urls, processors_count, time_durability).decode("utf-8")


        print ("UPDATE user_money SET money = {} WHERE user = '{}'".format(money, user_login))
        print ("INSERT INTO user_order_id (user, order_id) VALUES('%s', '%s');" % (user_login, order_id))

        conn.execute("UPDATE user_money SET money = {} WHERE user = '{}'".format(money, user_login))
        conn.execute("INSERT INTO user_order_id (user, order_id) VALUES('%s', '%s');" % (user_login, order_id))
        conn.commit()

        kwargs['money'] = money
        kwargs['order_id'] = order_id
        conn.close()
        return render_template("index.html", **kwargs)

    if result_form.validate_on_submit():

        user_login = str(result_form.user_login.data)
        order_id = str(result_form.order_id.data)
                
        cursor = conn.execute("SELECT * FROM user_order_id WHERE user = '{}' AND order_id = '{}'".format(user_login, order_id))
        exist = False
        for row in cursor:
            exist = True

        if exist == False:
            kwargs['task_status'] = 'You cant access this task'
            kwargs['task_result'] = 'Not available'
            conn.close()
            return render_template("index.html", **kwargs)

        result = get_result(order_id)
        if result.status == 0:
            kwargs['task_status'] = 'DONE'
        if result.status == 1:
            kwargs['task_status'] = 'UNDONE'
        if result.status == 2:
            kwargs['task_status'] = 'FAILED'

        if result.status == 0:
            kwargs['task_result'] = result.result
        else:
            kwargs['task_result'] = 'Not available'

        conn.close()
        return render_template("index.html", **kwargs)

    conn.close()
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
