FROM python:3.7.8-alpine3.12

COPY ./ /python/

WORKDIR /python

RUN pip install -r requirements.txt

CMD ["python","api.py"]