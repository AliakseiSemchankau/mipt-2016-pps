from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class SimilarsForm(Form):
    sb_band = TextField('band', validators = [Required()])
    sb_track = TextField('track')
    sb_limit = TextField('limit')
    sb_pref = TextField('pref')

class VkPostsForm(Form):
    vp_band = TextField('band', validators = [Required()])
    vp_limit = TextField('limit')
    vp_track = TextField('track')
    vp_pref = TextField('pref')

class OrderForm(Form):
    sub_tasks_urls = TextField('subtasks urls', validators=[Required()])
    processors_count = IntegerField('number of processors', validators=[Required()])
    time_durability = IntegerField('time, seconds', validators=[Required()])
