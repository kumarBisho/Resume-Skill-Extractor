FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    libx11-dev \
    libxext-dev \
    libxrender-dev \
    libx11-xcb-dev \
    libxcb1-dev \
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY resume_parser.py .
COPY templates/ templates/

# Create uploads directory
RUN mkdir -p /app/uploads

# Expose ports
EXPOSE 5000

# Command to run the application
CMD ["python", "resume_parser.py"]
