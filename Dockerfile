FROM python:3.12-slim
WORKDIR /app
RUN pip freeze > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY data-generator.py .
CMD ["python", "data-generator.py"]
