###
# filesystem
import sys
import os

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,directory)
###
# run that baby
from server import initialize,db
#from server.models import *

app = initialize(os.getenv('FLASK_CONFIG') or 'local')
import server.context

if app.config['PRINT_ENV']:
  print(' * Config: {0}'.format(app.config['ENVIRONMENT']))

### {{{ shell commands
import click
@app.cli.command()
@click.argument('target',required=False)
def ping(target):
  print('pong!')
  if target is not None:
    print('with love from {0}'.format(target))
### }}}
