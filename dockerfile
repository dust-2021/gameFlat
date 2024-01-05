FROM python:3.9
COPY . .
RUN pip install -r requirements/default.requirements.txt
EXPOSE 5000:5000
CMD gunicorn -c config/appConf/gunicorn.conf.py app:app
