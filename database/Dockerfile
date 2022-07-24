FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD database.py /app/database.py

ADD top250-00-19.csv /app/top250-00-19.csv

WORKDIR /app/

CMD python3 database.py