from flask import render_template, flash, redirect
from app import app
from .forms import *
import pickle

def send_order(subtasks_urls, processors_count, time_durability):
    # with open('../configuration.txt', 'r') as f:
    #     address = f.read().split('=')[1]
    return 265



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    order_form = OrderForm()

    kwargs = {'order_form': order_form}

    if order_form.validate_on_submit():

        sub_tasks_urls = str(order_form.sub_tasks_urls.data).split(' ')
        processors_count = int(order_form.processors_count.data)
        time_durability = int(order_form.time_durability.data)

        print ('sub_tasks_urls=', str(sub_tasks_urls))
        print (processors_count)
        print (time_durability)

        order_id = send_order(sub_tasks_urls, processors_count, time_durability)

        kwargs['order_id'] = order_id

        return render_template("ind.html", **kwargs)

    return render_template("ind.html", **kwargs)



