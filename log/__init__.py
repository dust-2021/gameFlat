import logging
import os

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import *
else:
    from config.appConf.flaskConf import *

# the basic logger
log = logging.getLogger('base')
log.setLevel(logging.INFO)
std_handler = logging.StreamHandler()
std_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler(filename=LOG_FILE + '/base_log.log', encoding='utf-8', mode='a+')
file_handler.setLevel(logging.INFO)
fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
std_handler.setFormatter(fmt)
file_handler.setFormatter(fmt)
log.addHandler(std_handler)
log.addHandler(file_handler)

# initialize function called logger
func_log = logging.getLogger('funcLogger')
func_log.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_FILE + '/func_log.log', mode='a+', encoding='utf-8')
fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
handler.setFormatter(fmt)
handler.setLevel(logging.INFO)
func_log.addHandler(handler)

# initialize user logger
user_log = logging.getLogger('user')
user_log.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_FILE + 'log/user_log.log', mode='a+', encoding='utf-8')
fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
handler.setFormatter(fmt)
handler.setLevel(logging.INFO)
user_log.addHandler(handler)
