FROM continuumio/anaconda3:latest
ENV RABBIT_SERVER=some-rabbit
RUN apt-get update
RUN pip install celery
COPY . celery-demo
WORKDIR celery-demo
RUN chmod +x run-celery.sh