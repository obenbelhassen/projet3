FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD /templates/print_items.html /app//templates/print_items.html

ADD /templates/result.html /app//templates/result.html

ADD api.py /app/api.py

WORKDIR /app/

EXPOSE 5000

CMD python3 api.py