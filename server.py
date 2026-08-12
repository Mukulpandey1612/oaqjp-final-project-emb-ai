"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/")
def render_homepage():
    """Render the application homepage."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_analysis():
    """Analyze the emotion of the submitted text."""
    text_to_analyze = request.args.get("textToAnalyze")

    analysis_result = emotion_detector(text_to_analyze)

    if analysis_result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        "For the given statement, the system response is "
        f"'anger': {analysis_result['anger']}, "
        f"'disgust': {analysis_result['disgust']}, "
        f"'fear': {analysis_result['fear']}, "
        f"'joy': {analysis_result['joy']} and "
        f"'sadness': {analysis_result['sadness']}. "
        f"The dominant emotion is {analysis_result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    