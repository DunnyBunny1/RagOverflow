# Use Python as our base image
FROM python:3.12-slim

# Set /frontend_code as our working directory. This matches our
# volume mount point we defined in the docker-compose file
WORKDIR /frontend_code

# Copy over our requirements file into img's working dir
# and do not cache the requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 (default StreamLit port) from the container 
EXPOSE 8501

# Run the StreamLit home.py (home page) file at runtime
# Run on port 8501 and make the server accessible on all network interfaces
# (0.0.0.0), ensuring srever accessible from outside container
CMD ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]
