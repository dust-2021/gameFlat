FROM python:3.9
COPY . .
CMD pip install -r requirements/default.requirements.txt
RUN gunicorn -c config/appConf/gunicorn.conf app:app