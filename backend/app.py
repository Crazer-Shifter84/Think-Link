from flask import Flask, jsonify

app = Flask("ThinkLink")

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ThinkLink API 🚀",
        "status": "running"
    })

@app.route("/devices")
def devices():
    sample_devices = [
        {"id": 1, "model": "ThinkPad T420", "cpu": "i5-2520M", "ram": "8GB"},
        {"id": 2, "model": "ThinkPad X230", "cpu": "i7-3520M", "ram": "16GB"},
        {"id": 3, "model": "ThinkPad T480", "cpu": "i5-8350U", "ram": "16GB"}
    ]
    return jsonify(sample_devices)

if __name__ == "__main__":
    app.run(debug=True)