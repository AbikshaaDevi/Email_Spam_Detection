# Email Spam Detection Using Flask & Naive Bayes

A simple Flask web app that detects whether an email is spam or not using a trained Naive Bayes model.

---

##  Overview

This project loads a dataset (`spam_or_not_spam.csv`), trains a Naive Bayes classifier on preprocessed email text, and provides a web interface for users to input email content and get spam predictions.

---

##  Features

- Text vectorization using `scikit-learn`'s `CountVectorizer` or `TfidfVectorizer`.
- Model training with `MultinomialNB` from `scikit-learn`.
- Web interface built with Flask:
  - Input box for email content.
  - Outputs spam or not spam prediction.
- Model and vectorizer are stored in `.pkl` files for quick loading.

---

##  Project Structure

```
Email_Spam_Detection/
│
├── app.py
├── Spam_Detection.ipynb
├── spam_or_not_spam.csv
├── nb_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── templates/
    └── index.html
```

---

##  Setup & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/AbikshaaDevi/Email_Spam_Detection.git
   cd Email_Spam_Detection
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app locally**  
   ```bash
   python app.py
   ```
   Then open your browser and go to `http://127.0.0.1:5000/`.

4. **Make a prediction**  
   Paste email text into the input box and click **Predict**.  
   The app will display whether the email is **Spam** or **Not Spam**.

---

##  Deployment

You can deploy this app on platforms like Render or Heroku. Just upload your project files, set up Python environment, and start the Flask server.

---

##  About the Author

This project was created by **Abikshaa Devi** as a demonstration of building a simple text classification model with Flask.

---

##  Contribution

Feel free to:
- Improve preprocessing (stopwords removal, stemming, lemmatization).
- Add more robust vectorization like `TfidfVectorizer`.
- Enhance UI/UX.

---

##  License

This project is open source—feel free to use it freely.
