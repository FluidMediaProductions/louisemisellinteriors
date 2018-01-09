FROM python:3.6

RUN apt-get update
RUN apt-get install -y blender

COPY requirements.txt /
RUN pip3 install -U pip
RUN pip3 install -Ur requirements.txt

COPY . /code

WORKDIR /code
CMD ./start.sh