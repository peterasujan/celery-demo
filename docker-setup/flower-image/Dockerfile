FROM continuumio/anaconda3:latest
ENV RABBIT_SERVER=some-rabbit
RUN git clone https://github.com/peterasujan/celery-demo.git
RUN apt-get update
RUN pip install celery
RUN pip install flower
#RUN mkdir test_celery
#COPY test_celery test_celery
WORKDIR celery-demo
EXPOSE 5555
CMD ["test_celery/run-flower.sh"]