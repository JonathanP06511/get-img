FROM python:3.12-slim

WORKDIR /app

COPY src/requirements.txt requirements.txt
COPY src/ .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3012

CMD ["python", "app.py"]
