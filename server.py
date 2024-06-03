from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")

def emotionDetector():

    text_To_Analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_To_Analyze)
    dominant_emotion = response['dominant_emotion']
    del response['dominant_emotion']
    str_response = ', '.join(f'{k}:{v}' for k, v in response.items())
        
    return f"For the given statement, the system response is {str_response}. The dominant emotion is {dominant_emotion} "

@app.route("/")

def index():
    return render_template("index.html")

    
#if __name__==" __main__":
app.run(host="0.0.0.0", port = 5000)