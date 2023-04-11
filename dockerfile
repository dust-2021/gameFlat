FROM python:3.9
COPY . .
CMD pip install -r requirements/default.requirements.txt