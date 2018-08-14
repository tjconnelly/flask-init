activate_this = '../bin/activate_this.py'
with open(activate_this) as file_:
  exec(file_.read(), dict(__file__=activate_this))

import sys
import os

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,directory)

from www import initialize
application = initialize()
