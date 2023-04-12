"""
Author: li bo
date: 2023/4/10 11:29
"""
import logging

log = logging.getLogger('base')
std_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename='log/base_log.log', encoding='utf-8', mode='a+')
fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
std_handler.setFormatter(fmt)
std_handler.setLevel(logging.INFO)
file_handler.setFormatter(fmt)
file_handler.setLevel(logging.INFO)
log.addHandler(std_handler)
log.addHandler(file_handler)

# 初始化函数日志对象
func_log = logging.getLogger('funcLogger')
handler = logging.FileHandler('log/func_log.log', mode='a+', encoding='utf-8')
fmt = logging.Formatter('%(name)s %(asctime)s: %(levelname)s -- %(message)s')
handler.setFormatter(fmt)
handler.setLevel(logging.INFO)
func_log.addHandler(handler)