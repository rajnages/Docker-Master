# Step 1: Use the official Python image from Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt /app/

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . /app/

# Step 6: Define the command to run your application
CMD ["python", "app.py"]

# Optionally, expose a port if your app runs a web server (e.g., Flask)
# EXPOSE 5000
