# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all source code to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command runs the producer service; override at runtime as needed
CMD ["python", "producer/producer.py"]
