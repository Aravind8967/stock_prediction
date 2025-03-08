FROM python:3.8

WORKDIR /app

COPY . .

RUN apt-get update; apt-get upgrade -y; apt-get install -y sudo iputils-ping vim nano

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]
