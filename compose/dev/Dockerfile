FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python3.9 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python3.9 manage.py runserver 0.0.0.0:8000