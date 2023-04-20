"""
Author: li bo
date: 2023/4/10 11:29
"""
import logging

log = logging.getLogger('base')
log.setLevel(logging.INFO)
std_handler = logging.StreamHandler()
std_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler(filename='log/base_log.log', encoding='utf-8', mode='a+')
file_handler.setLevel(logging.INFO)
fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
std_handler.setFormatter(fmt)
file_handler.setFormatter(fmt)
log.addHandler(std_handler)
log.addHandler(file_handler)

# 初始化函数日志对象
func_log = logging.getLogger('funcLogger')
func_log.setLevel(logging.INFO)
handler = logging.FileHandler('log/func_log.log', mode='a+', encoding='utf-8')
fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
handler.setFormatter(fmt)
handler.setLevel(logging.INFO)
func_log.addHandler(handler)

# 初始化用户日志对象
user_log = logging.getLogger('user')
user_log.setLevel(logging.INFO)
handler = logging.FileHandler('log/user_log.log', mode='a+', encoding='utf-8')
fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
handler.setFormatter(fmt)
handler.setLevel(logging.INFO)
user_log.addHandler(handler)
