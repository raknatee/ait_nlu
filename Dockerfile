FROM python:3.9.4-buster
WORKDIR /home/src

RUN pip install pdfminer.six

COPY ./src /home/src

CMD tail -f /dev/null