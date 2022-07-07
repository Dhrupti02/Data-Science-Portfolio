from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('baggingclassifier.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        economic_cond_national = int(request.form['economic_cond_national'])
        economic_cond_household = int(request.form['economic_cond_household'])
        Blair = int(request.form['Blair'])
        Hague = int(request.form['Hague'])
        Europe = int(request.form['Europe'])
        political_knowledge = int(request.form['political_knowledge'])

        prediction=model.predict([[age, economic_cond_national, economic_cond_household, Blair, Hague, Europe, political_knowledge]])
        
        if prediction == 1:
            output = 'Labour'
        else:
            output = 'Conservative	'
        if not output:
            return render_template('index.html',prediction_texts="Sorry")
        else:
            return render_template('index.html',prediction_text="The user will vote to {} party.".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)