from flask import Flask
from flask.ext.misaka import Misaka # Markdown support


app = Flask(__name__)   # this app is the variable which gets assigned the Flask instance
app.config.from_object('config')    # do this after the Flask object is created
Misaka(app) # wrap Flask instance with the Misaka class

#### database connection ####
from pymongo import *
con = Connection()
db = con.blog

#### moment.js####
#from .momentjs import momentjs
#app.jinja_env.globals['momentjs'] = momentjs    # this just tells Jinja2 to expose our class as a global variable to all templates

# should be placed at the botton of __init__.py
from app import views   # this app is the package from which we import the views module
