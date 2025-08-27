from flask import Flask, jsonify, request

app = Flask("Think-Link")

# Store only ThinkPads
thinkpads = []

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ThinkLink API 🖥️",
        "status": "running",
        "supported": "All ThinkPad models",
        "total_devices": len(thinkpads)
    })

# ✅ Get all ThinkPads
@app.route("/thinkpads", methods=["GET"])
def get_thinkpads():
    return jsonify({"thinkpads": thinkpads})

# ✅ Add a new ThinkPad
@app.route("/thinkpads", methods=["POST"])
def add_thinkpad():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "ThinkPad 'name' is required"}), 400
    
    if "ThinkPad" not in data["name"]:
        return jsonify({"error": "Only ThinkPads are supported"}), 400

    thinkpad = {
        "id": len(thinkpads) + 1,
        "name": data["name"],               # e.g., "ThinkPad T420"
        "series": data.get("series", "N/A"),# optional: T, X, P, etc.
        "status": data.get("status", "offline")
    }
    thinkpads.append(thinkpad)
    return jsonify({"message": "ThinkPad added", "thinkpad": thinkpad}), 201

# ✅ Update ThinkPad
@app.route("/thinkpads/<int:tp_id>", methods=["PUT"])
def update_thinkpad(tp_id):
    for tp in thinkpads:
        if tp["id"] == tp_id:
            data = request.get_json()
            tp["name"] = data.get("name", tp["name"])
            tp["series"] = data.get("series", tp["series"])
            tp["status"] = data.get("status", tp["status"])
            return jsonify({"message": "ThinkPad updated", "thinkpad": tp})
    return jsonify({"error": "ThinkPad not found"}), 404

# ✅ Delete ThinkPad
@app.route("/thinkpads/<int:tp_id>", methods=["DELETE"])
def delete_thinkpad(tp_id):
    global thinkpads
    thinkpads = [tp for tp in thinkpads if tp["id"] != tp_id]
    return jsonify({"message": f"ThinkPad {tp_id} deleted"})

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
