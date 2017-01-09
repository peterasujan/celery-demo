FROM continuumio/anaconda3:latest
ENV RABBIT_SERVER=some-rabbit
RUN apt-get update
RUN pip install celery
RUN pip install flower
COPY . celery-demo
WORKDIR celery-demo
RUN chmod +x run-flower.sh
EXPOSE 5555
CMD ["./run-flower.sh"]