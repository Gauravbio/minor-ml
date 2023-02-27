from flask import Flask,jsonify,request
from deepface import DeepFace
import base64
from flask_cors import CORS,cross_origin

app=Flask(__name__)
CORS(app)
cors=CORS(app,resources={r"/*": {"origins":"*"}})


@app.route('/')
def home():
    return jsonify({"message":"Hello Flask"})

@app.route('/emotion',methods=['POST'])
@cross_origin()
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

if __name__=="__main__":
    app.debug=True
    app.run("0.0.0.0",port=5000)
