FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python3-pip python3
RUN pip3 install -U pip

COPY requirements.txt /
RUN pip3 install -Ur /requirements.txt

COPY . /code

WORKDIR /code
CMD /code/run.sh