from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello(): 
    return "Hello World from Flask"

@app.route("/example")
def example(): 
    return jsonify({
        "message" : "Welcome to an example page"
    })

if __name__ == "__main__":
    # Run our app in debug mode (to enable hot reloading)
    # on port 5000, listening on all network interfaces (0.0.0.0)
    # so that the server is accessible from our host machine
    app.run(host='0.0.0.0', port=5000, debug=True)