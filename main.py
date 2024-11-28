from flask import Flask, jsonify, request
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure logging to log all incoming requests
logging.basicConfig(level=logging.DEBUG)

# Define a route for the root URL
@app.route('/')
def hello_world():
    app.logger.info('Root endpoint hit')
    return jsonify(message="Hello, Docker!")

# Define a route for another endpoint
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    app.logger.info(f'Greet endpoint hit with name: {name}')
    return jsonify(message=f"Hello, {name}!")

# Health check route to verify if the service is up and running
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="UP")

# Route to handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Not Found", message="The requested URL was not found on the server."), 404

# Route to handle invalid JSON or other errors
@app.errorhandler(400)
def bad_request(e):
    return jsonify(error="Bad Request", message="Invalid request data."), 400

# Define a route to accept JSON data via POST request
@app.route('/json', methods=['POST'])
def post_json():
    data = request.get_json()
    if not data:
        return jsonify(error="Bad Request", message="No JSON provided"), 400
    app.logger.info(f'POST request with JSON data: {data}')
    return jsonify(message="Received JSON", data=data), 200

# Start the application
if __name__ == '__main__':
    # Allow port to be configured via environment variable
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if not set
    app.run(host='0.0.0.0', port=port)
