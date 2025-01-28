# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /C:\Users\91700\Desktop\My_Project_1

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Command to run your Flask app
CMD ["python", "app/app.py"]
