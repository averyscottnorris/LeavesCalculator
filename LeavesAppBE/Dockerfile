FROM python:3-buster

RUN mkdir -p /app/src

WORKDIR /app/src

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

#Start app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]