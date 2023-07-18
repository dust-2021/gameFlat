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
log_file = os.path.abspath('/var/log/gunicorn')
if not os.path.exists(log_file):
    os.mkdir(log_file)
accesslog = log_file + '/access.log'
errorlog = log_file + '/error.log'
