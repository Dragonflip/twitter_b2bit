FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /twitter_api
WORKDIR /twitter_api
COPY . /twitter_api/
RUN pip install -r requirements.txt
