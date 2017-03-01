FROM python:2.7

MAINTAINER Ondrej Sika <ondrej@ondrejsika.com>

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
RUN pip install gunicorn

WORKDIR /app
CMD gunicorn --bind 0.0.0.0:80 wsgi:application
