FROM python:3.10-slim

# Install system dependencies first
RUN apt-get update && \
    apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 ffmpeg

# Set the working directory and copy files into the image
WORKDIR /app
COPY . .

# Now it's safe to install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "main.py"]
