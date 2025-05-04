# Use Python as our base image 
FROM python:3.12-slim

# Set /backend_code as our working directory. This matches our
# volume mount point we defined in the docker-compose file
WORKDIR /backend_code

# Install dependencies
# curl is needed for the health check for the Flask server 
RUN apt-get update && apt-get install -y curl && apt-get clean

# Copy over our requirements file into img's working dir
# and do not cache  the requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (default Flask port) from the container 
EXPOSE 5000 

# Run the Flask app.py file at runtime 
CMD ["python3", "api/app.py"]