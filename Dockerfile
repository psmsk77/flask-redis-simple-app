FROM python:3.10-alpine3.17

RUN pip3 install flask redis

COPY . /opt/

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=5000
