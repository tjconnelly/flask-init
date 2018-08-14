from . import core
from server import context

from flask import g,request,render_template,url_for,jsonify

import datetime

@core.before_request
def before_request():
  context.beforerequest()

### index
@core.route('/',methods=['GET'])
@core.route('/content/<path:navpath>',methods=['GET'])
def index(navpath=None,content=None):
  return render_template('index.html',content=content)
