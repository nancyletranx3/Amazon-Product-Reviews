from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open("rus_svc_ngram.sav", "rb"))

@app.route("/sentiment", methods = ["post"])
def sentiment():
    review = [request.json["review"]]
    predictions = model.predict(review)
    return jsonify({"pred": predictions[0]})


if (__name__ == "__main__"):
    app.run(debug = True)
