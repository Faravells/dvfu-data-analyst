FROM python:3.12-slim
WORKDIR /app
RUN pip install mysql-connector-python==8.0.33
COPY data-generator.py .
CMD ["python", "data-generator.py"]
