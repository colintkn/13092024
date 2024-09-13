# Use the official Python image from the DockerHub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any dependencies from requirements.txt
RUN pip install -r requirements.txt

# Make port 5656 available to the world outside this container
EXPOSE 5656

# Define environment variable
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5656"]
