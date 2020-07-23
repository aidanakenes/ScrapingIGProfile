FROM python:3.8

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY ./src ./src

EXPOSE 8080

CMD python3 src/main.py
