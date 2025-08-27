from flask import Flask, jsonify

app = Flask(Think-Link)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ThinkLink API 🚀",
        "status": "running"
    })

if __name__ == "__main__":
    app.run(debug=True)