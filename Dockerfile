# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir pandas

# Run load_csv_to_sqlite.py when the container launches
ENTRYPOINT ["python", "load_csv_to_sqlite.py"]
