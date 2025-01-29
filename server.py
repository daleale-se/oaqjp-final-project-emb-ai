"""
server.py - Flask server for Emotion Detection API.
Provides endpoints for analyzing emotions in text.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    """Analyzes emotions in the given text and returns the detected emotions."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"]:
        return (
            f"For the given statement, the system response is " 
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}," 
            f"'fear': {response['fear']}, 'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. The dominant emotion is "
            f"{response['dominant_emotion']}."
        )
    return "Invalid text! Please try again!."
@app.route("/")
def render_index_page():
    """Renders the index.html page."""
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
