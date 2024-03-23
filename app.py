from flask import Flask, request, jsonify
from model import get_prediction_from_url, main


app = Flask(__name__)

@app.route('/model_prediction', methods=['POST'])
def model_prediction():
    data = request.get_json()
    url = data['url']

    if url.startswith("https://"):
        url = url.split("https://", 1)[-1]
    elif url.startswith("http://"):
        url = url.split("http://", 1)[-1]

    features = main(url)

    prediction = get_prediction_from_url(url)

    return jsonify({'prediction': prediction})
    
@app.route('/', methods=['GET'])
def  hello():
    return "Hello World!"
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 5008)
