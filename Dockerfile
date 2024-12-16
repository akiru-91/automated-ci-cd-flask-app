# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "src/main.py"]
