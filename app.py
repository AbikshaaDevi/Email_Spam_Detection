from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("nb_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        email = request.form['email']
        email_vec = vectorizer.transform([email])
        prediction = model.predict(email_vec)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
