from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow CORS
CORS(app)


@app.route('/location', methods=['POST'])
def location():
    try:
        data = request.get_json(force=True, silent=True)

        if not data:
            print("❌ No data received")
            return jsonify({"error": "No data"}), 400

        # 🌐 Get real client IP (handles proxies like Railway)
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)

        # 📍 Get location data
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        accuracy = data.get('accuracy')

        # 🧠 Optional extra info
        user_agent = request.headers.get('User-Agent')

        # 🖨️ Logs
        print("\n===== NEW REQUEST =====")
        print(f"🌐 IP Address: {ip}")
        print(f"📍 Latitude: {latitude}")
        print(f"📍 Longitude: {longitude}")
        print(f"🎯 Accuracy: {accuracy}")
        print(f"🧾 User-Agent: {user_agent}")
        print("=======================\n")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("🔥 Error:", str(e))
        return jsonify({"error": "Server error"}), 500


# Railway-compatible port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
