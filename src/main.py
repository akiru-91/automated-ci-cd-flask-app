from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the CI/CD Automated Deployment!",
        "status": "success"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy"
    })

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({
        "message": f"Hello, {name}!",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
