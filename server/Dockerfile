FROM python:alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["uvicorn",  "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
