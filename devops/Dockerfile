FROM python:3.7-slim

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

ADD . /app

CMD [ "python", "server.py" ]
