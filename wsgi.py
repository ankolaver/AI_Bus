'''
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

from mla import app as mla
import flask_app

application = DispatcherMiddleware(flask_app, {
    '/mla': mla.server,
    
})  

if __name__ == '__main__':
    run_simple('localhost', 8050, application)  '''