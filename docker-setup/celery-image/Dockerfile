FROM continuumio/anaconda3:latest
ENV RABBIT_SERVER=some-rabbit
RUN git clone https://github.com/peterasujan/celery-demo.git
RUN apt-get update
RUN pip install celery
#RUN mkdir test_celery
#COPY test_celery/ test_celery/
WORKDIR celery-demo
CMD ["/bin/bash"]