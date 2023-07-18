# Use official Python runtime as base image
FROM python:3.10.6

# Set the working directory in the container to /app
WORKDIR /app

# Copy code and config files
COPY src /app/src
COPY requirements.txt /app
COPY config.json /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application when the container launches
CMD ["python", "src/cli.py"]
