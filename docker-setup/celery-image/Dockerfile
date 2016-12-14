FROM continuumio/anaconda3:latest
ENV RABBIT_SERVER=some-rabbit
RUN git clone https://github.com/peterasujan/celery-demo.git
RUN apt-get update
RUN pip install celery
WORKDIR celery-demo
CMD ["/bin/bash"]