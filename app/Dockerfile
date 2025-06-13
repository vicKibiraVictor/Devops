# Use a slim Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app.py .

# Copy input folder (contains input.csv)
COPY input/ ./input/

# Make sure the output directory exists
RUN mkdir -p output

# Run the script
CMD ["python", "app.py"]
