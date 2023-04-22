FROM python:3.11

LABEL author="ff.primrose@gmail.com"
LABEL maintainer="ff.primrose@gmail.com"

COPY . /app/server

WORKDIR /app/server

RUN pip3 install -r requirements.txt

RUN python setup.py install
RUN python setup.py build

ENTRYPOINT ["python", "main.py"]


