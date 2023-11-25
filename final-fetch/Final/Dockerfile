# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Install any needed packages
RUN pip install --no-cache-dir dill

# Copy requirements.txt to the working directory
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the application
CMD ["python", "-c", "from app import load_model, app; load_model(); app.run(host='0.0.0.0', port=5000)"]
