from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow CORS (you can restrict later)
CORS(app)

@app.route('/location', methods=['POST'])
def location():
    try:
        # Safely get JSON
        data = request.get_json(force=True, silent=True)

        if not data:
            print("❌ No data received")
            return jsonify({"error": "No data"}), 400

        latitude = data.get('latitude')
        longitude = data.get('longitude')
        accuracy = data.get('accuracy')

        # Log output (visible in Railway logs)
        print(f"📍 Latitude: {latitude}")
        print(f"📍 Longitude: {longitude}")
        print(f"🎯 Accuracy: {accuracy}")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("🔥 Error:", str(e))
        return jsonify({"error": "Server error"}), 500


# Railway-compatible port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)