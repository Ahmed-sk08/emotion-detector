import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    status_code = response.status_code
    
    if status_code == 400:
        formatted_output = { 'anger': None,
                             'disgust': None,
                             'fear': None,
                             'joy': None,
                             'sadness': None,
                             'dominant_emotion': None }

    else:
        # Extract emotions
        emotions = response_json['emotionPredictions'][0]['emotion']
        
        # Determine dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        # Format the output
        formatted_output = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
    
    return formatted_output
