import os
import env
from configparser import SafeConfigParser

def config_path():
  return os.path.dirname(os.path.realpath(__file__))

def config_env():
  try:
    return env.ENVIRONMENT
  except AttributeError:
    package,environment = os.path.basename(config_path()).split("-")
    return environment

def config_database(env=None):
  if env is None:
    env = config_env()
  db = {};
  db[env] = db.get(env,{});
  parser = SafeConfigParser();
  parser.read(os.path.join(config_path(),'database.config'))
  for key,value in parser.items(env):
    db[env][key] = value;
  connection = db[env];
  return connection;

def config_sqlalchemy(cxn):
  uri = 'mysql+pymysql://{user}:{passwd}@{host}/{db}'.format(**cxn)
  return uri

def config_lcdn(env):
  resource_urls = {}
  parser = SafeConfigParser();
  parser.read(os.path.join(config_path(),'lcdn.cfg'))
  for key,value in parser.items(env):
    resource_urls[key] = value;
  return resource_urls

class Config:
  NAME = env.APPNAME
  # setup
  DIRECTORY = config_path()
  ENVIRONMENT = config_env()
  # data comes from somewhere
  DATABASE = config_database()
  # sqlalchemy
  SQLALCHEMY_DATABASE_URI = config_sqlalchemy(DATABASE)
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  # deliver libraries
  #LCDN_PATH = os.path.join(config_path(),'/lcdn/static')
  #LCDN_ALLOWED = {
  #  'css':  'text/css',
  #  'js': 'application/javascript'
  #}
  #LCDN_SRC = config_lcdn('remote')
  # form support
  SECRET_KEY = ''
  # unicode on
  JSON_AS_ASCII = False
  # debugging off
  DEBUG = False
  TESTING = False
  PRINT_ENV = False
 
# config modifications
class LiveConfig(Config):
  JSON_AS_ASCII = False

class DevConfig(Config):
  DEBUG = True
  TESTING = True
  PRINT_ENV = True

class LocalConfig(Config):
  DEBUG = True
  TESTING = True
  PRINT_ENV = True
  #LCDN_SRC = config_lcdn('local')
  #LCDN_SRC = config_lcdn('remote')

configs = {
  "live":         "config.LiveConfig",
  "local":        "config.LocalConfig",
  "dev":          "config.DevConfig",
  "development":  "config.DevConfig",
  "experimental": "config.DevConfig",
  "default":      "config.DevConfig"
}
