
# for Flask-WTF extension
WTF_CSRF_ENABLED = True # activates the cross-site request forgery prevention, is enabled by default
SECRET_KEY = 'you-will-never-guess' # creat a cryptographic token  that is used to validate a form

import os
basedir = os.path.abspath(os.path.dirname('__file__'))
