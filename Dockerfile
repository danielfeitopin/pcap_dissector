# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install tshark
RUN apt-get update && \
    apt-get install -y tshark && \
    rm -rf /var/lib/apt/lists/*

# Command to run the application
CMD ["python3", "-m", "gunicorn", "-w", "2", "-b", "0.0.0.0", "webapp:app"]