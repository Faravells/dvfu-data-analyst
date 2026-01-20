FROM python:3.12
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY data-generator.py .
CMD ["python", "data-generator.py"]
