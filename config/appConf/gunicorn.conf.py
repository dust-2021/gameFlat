import multiprocessing

# workers = multiprocessing.cpu_count() * 2 - 1
workers = 1
threads = 1

bind = '0.0.0.0:5000'
worker_class = 'eventlet'
worker_connections = 500
loglevel = 'info'
daemon = True

pidfile = './info/pid'
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
