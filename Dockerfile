# Use the official Python 3.11 image from the Docker Hub.
# This runs on Debian Linux.
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY python/ /app

# Set environment variables
ENV ENVIRONMENT dev
ENV OPENAI_API_KEY ""

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Run the application when the container launches
CMD ["python", "console.py"]
