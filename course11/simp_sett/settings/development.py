import os

DEBUG = True
SECRET_KEY = os.environ['S']
WTF_CSRF_ENABLED = False