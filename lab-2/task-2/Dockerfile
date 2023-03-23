
FROM python:3.10-slim

COPY requirements.txt .
RUN python -m pip install -r requirements.txt --no-cache

WORKDIR /app
COPY . /app


CMD ["python", "./main.py"]
