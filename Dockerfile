# Use the official Python image from the Docker Hub
FROM python:3.12-slim
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt .
# Install the dependencies
RUN pip install -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
# Expose the port the app runs on (change to port 4000)
EXPOSE 4000
# Run the application
CMD ["python", "app.py"]