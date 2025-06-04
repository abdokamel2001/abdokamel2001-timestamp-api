from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "UNIX to Date API is running!"

@app.route("/convert", methods=["GET"])
def convert_unix_to_date():
    unix_time = request.args.get("timestamp")
    if not unix_time:
        return jsonify({"error": "timestamp query parameter is required"}), 400

    try:
        unix_time = int(unix_time)
        human_date = datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
        return jsonify({
            "unix": unix_time,
            "readable": human_date
        })
    except ValueError:
        return jsonify({"error": "Invalid UNIX timestamp"}), 400

if __name__ == "__main__":
    app.run(debug=True)
