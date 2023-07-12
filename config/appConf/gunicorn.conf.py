import multiprocessing
import os

# workers = multiprocessing.cpu_count() * 2 - 1
workers = 1
threads = 1

bind = '0.0.0.0:5000'
worker_class = 'eventlet'
worker_connections = 500
loglevel = 'info'
daemon = False

pidfile = './info/pid'
if not os.path.exists('/var/log/gunicorn'):
    os.mkdir('/var/log/gunicorn')
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
