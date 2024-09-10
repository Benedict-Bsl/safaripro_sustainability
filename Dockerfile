FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN apk update && apk add python3-dev gcc libc-dev libffi-dev && \
  pip install --upgrade pip && \
  pip install -r /app/requirements.txt && \
  pip install --upgrade markdown


# Copy rest of the application
COPY . /app/
EXPOSE 8000

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

CMD python3 manage.py runserver 0.0.0.0:8000
