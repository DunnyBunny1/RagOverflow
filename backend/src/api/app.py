from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def hello(): 
    return "Hello World from Flask"

@app.route("/example")
def example(): 
    return jsonify({
        "message" : "Welcome to an example page"
    })

@app.route("/health_check")
def health_check():
    """
    Health check to ensure the server is running successfully. Returns the message "OK"
    with the "200 OK" status code 
    """
    return make_response(
        "OK", 200
    )
    

if __name__ == "__main__":
    # Run our app in debug mode (to enable hot reloading)
    # on port 5000, listening on all network interfaces (0.0.0.0)
    # so that the server is accessible from our host machine
    app.run(host='0.0.0.0', port=5000, debug=True)