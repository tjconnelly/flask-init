from . import core
from appname import context

#from flask import current_app as app
from flask import g,request,render_template,url_for,jsonify

import datetime

@app.before_request
def before_request():
  context.beforerequest()

### index
@app.route('/',methods=['GET'])
@app.route('/content/<path:navpath>',methods=['GET'])
def index(navpath=None,content=None):
  return render_template('index.html',content=content)
