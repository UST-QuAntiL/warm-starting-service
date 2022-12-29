FROM python:3.8-slim-buster

WORKDIR /warm-starting-service
COPY . /warm-starting-service

RUN pip3 install -r requirements.txt 

ENTRYPOINT [ "python" ]

CMD ["ws-app.py" ]