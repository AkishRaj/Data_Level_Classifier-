from flask import Flask, render_template, request
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_text = request.form["data"]
        text_vec = vectorizer.transform([user_text])
        prediction = model.predict(text_vec)[0]
        result = prediction

    return render_template("index.html", result=result)

app.run(debug=True)
