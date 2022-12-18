FROM python:3.9.0-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt

COPY . /app/
EXPOSE 5000

ENTRYPOINT ["/app/docker-entrypoint.sh"]
