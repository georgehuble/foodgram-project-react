FROM python:3.8.5

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
