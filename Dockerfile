FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install pytest pytest-cov selenium
CMD ["python", "monitor.py"]
