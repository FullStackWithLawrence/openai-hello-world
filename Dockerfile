# Use the official Python 3.11 image from the Docker Hub.
# This runs on Debian Linux.
FROM python:3.12-slim-bookworm

# Set the working directory to /app
WORKDIR /dist

# Copy the current directory contents into the container at /app
COPY app /dist/app
COPY requirements/prod.txt requirements.txt

# Set environment variables
ENV ENVIRONMENT=dev
ENV PYTHONPATH=/dist

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Run the application when the container launches
CMD ["python", "app/hello_world.py"]
