# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to point to the Flask app file
ENV FLASK_APP=app.py  # Ensure this is correct for your app

# Expose the port the app will run on
EXPOSE 5000

# Run Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
