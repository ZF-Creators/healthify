# Use official Python 3.10 image
FROM python:3.10-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app files
COPY . /app/

# Expose port (Render expects this)
EXPOSE 5000

# Start the app using gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]
