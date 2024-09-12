FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app.py /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
