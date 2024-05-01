FROM python:3.10

WORKDIR /check_price

COPY ./requirements.txt /check_price/

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]
