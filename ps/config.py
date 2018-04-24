"""Application configuration.

When using app.config.from_object(obj), Flask will look for all UPPERCASE
attributes on that object and load their values into the app config. Python
modules are objects, so you can use a .py file as your configuration.
"""

import os

PWD = os.path.abspath(os.curdir)
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/ps.db'.format(PWD)
SECRET_KEY = 'passw0rd'
SESSION_PROTECTION = 'strong'
SQLALCHEMY_TRACK_MODIFICATIONS = True