from flask import Flask,jsonify,request
from deepface import DeepFace
import base64

app=Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message":"Hello Flask"})

@app.route('/emotion',methods=['POST'])
def emotionDetection():
    image=request.json['image']
    image=image[22:]
    decoded_image=base64.b64decode(image)

    with open("sample.png","wb") as out_file:
        out_file.write(decoded_image)

    print("model time")
    result=DeepFace.analyze('sample.png',actions=['emotion'])
    output=result[0]['dominant_emotion']
    return jsonify({"output":output})
