FROM python:3.11.2-bullseye

ARG BACKEND_URL

ENV BACKEND_URL=${BACKEND_URL}

RUN apt-get update

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
ENV PYTHONDONTWRITEBYTECODE=1
COPY . /app/

WORKDIR /app

EXPOSE 3000
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
