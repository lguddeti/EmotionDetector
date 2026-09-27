import requests

def emotionDetector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    print(" response_status_code>>>>>>", response.status_code)
    result = response.json()
    if response.status_code == 400:
        return {
            "anger": "None",
            "disgust": "None",
            "fear": "None",
            "joy": "None",
            "sadness": "None",
            "dominant_emotion": "None"
        }
    emotions = result["emotionPredictions"][0]["emotion"]
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }

print(emotionDetector("I am extremely happy today!"))
