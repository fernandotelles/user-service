FROM python:3.7-slim-stretch

# RUN apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV FLASK_APP=app.py

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app


RUN python /app/init_db.py

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]