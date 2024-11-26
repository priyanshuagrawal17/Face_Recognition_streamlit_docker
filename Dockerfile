# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies, including Git
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    libboost-all-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Define the command to run Streamlit
CMD ["streamlit", "run", "app.py"]
