from flask import Flask, request, render_template
import pickle

filename = 'model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv = pickle.load(open("transform.pkl", "rb"))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['q']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
    return render_template('index.html', pred='Emotion is {}'.format(my_prediction[0]))


if __name__ == "__main__":
    app.run(debug=True)
