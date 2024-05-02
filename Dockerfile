FROM python:3.10

WORKDIR /check_price

COPY ./requirements.txt /check_price/

RUN pip install -r requirements.txt

COPY . .
