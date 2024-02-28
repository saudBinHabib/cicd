# Use an official Python runtime as a parent image
FROM python:3.11.8-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ../ /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements/dev.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
