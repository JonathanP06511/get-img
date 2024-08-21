FROM python:3.12-slim

WORKDIR /app

RUN pip install flask flasgger

COPY . .

EXPOSE 3012

CMD ["python", "app.py"]
