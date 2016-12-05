from flask import Flask
from flask_bootstrap import Bootstrap
from .nav import nav

app = Flask(__name__)
app.config.from_object('order.flask.config')
Bootstrap(app)

# We initialize the navigation as well
nav.init_app(app)
