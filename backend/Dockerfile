# Dockerfile for backend (Flask app)
FROM python:3.8-alpine
WORKDIR /app
COPY . /app
RUN pip install Flask
EXPOSE 5000
CMD ["python", "app.py"]
