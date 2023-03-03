# Use the official Python image as base
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app/ .

# Set the environment variable for the Flask app
ENV SLACK_BOT_TOKEN = "xoxb-your-token"
ENV SLACK_APP_TOKEN = "xapp-your-token" 
ENV OPENAI_API_KEY = "sk-your-token"

# Expose the port that the app will run on
EXPOSE 5000

# Start the Flask app
CMD ["python3", "app.py"]