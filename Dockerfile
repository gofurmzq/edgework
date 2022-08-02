FROM python:3.7.13-buster

WORKDIR /project

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:5000", "app:app"]