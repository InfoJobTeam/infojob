FROM python:3-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /code
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD ./src/ .