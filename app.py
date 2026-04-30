from flask import Flask, render_template, request, jsonify
from predict import predict_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]
    result = predict_sentiment(text)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)