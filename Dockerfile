FROM python:3.9.4-buster
WORKDIR /home/src

RUN pip install pdfminer.six
RUN pip install stanza

COPY ./src /home/src

CMD tail -f /dev/null