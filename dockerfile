FROM python:3.9
FROM nginx
COPY . .
RUN pip install -r requirements/default.requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 5000:5000
CMD gunicorn -c config/appConf/gunicorn.conf.py app:app
