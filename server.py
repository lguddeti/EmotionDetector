"""
server.py
---------
Flask server for the Emotion Detection project.
Provides an API endpoint that accepts text input
and returns detected emotions as a JSON response.
"""
from flask import request, Flask, jsonify, render_template
from EmotionDetector.emotion_detection import emotionDetector


app = Flask(__name__)

@app.route("/")
def index():
    """
    Display a simple welcome message for the root endpoint.
    Returns:
        str: A plain-text message confirming the server is running.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    request.form.get("textToAnalyze", "")
    text = request.form.get("textToAnalyze", "")
    result = emotionDetector(text)
    return jsonify(result)

if __name__ == "__main__":
    """
    Run the Flask development server.
    Note:
        In Skills Network Labs, host must be '0.0.0.0'
        so the app is accessible via the public preview URL.
    """
    app.run(host="0.0.0.0", port=5000)
