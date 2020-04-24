FROM python:3.6.9

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

ENV PORT 8080
CMD ["gunicorn", "main:app", "--config=config.py"]