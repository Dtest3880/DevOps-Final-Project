FROM python:3.11-slim
# Set the working directory
WORKDIR /app
#install  Flask
RUN pip install --no-cache-dir flask
COPY . /app
# Expose the port Flask runs on
EXPOSE 5000
# Command to run the Flask app
CMD ["python", "app.py"]