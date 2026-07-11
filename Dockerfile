# Use a small Python image
FROM python:3.13-slim

# Set the working folder inside the container
WORKDIR /app

# Copy the dependency file first
COPY requirements.txt .

# Install the project libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and model files
COPY src/ src/
COPY models/ models/

# Open the port used by FastAPI
EXPOSE 8000

# Start the API when the container runs
CMD ["python", "-m", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]