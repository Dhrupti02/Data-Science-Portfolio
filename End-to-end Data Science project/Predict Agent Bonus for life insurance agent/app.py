from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        SumAssured = float(request.form['SumAssured'])
        SumAssured = np.log(SumAssured)

        Age = float(request.form['Age'])

        MonthlyIncome = float(request.form['MonthlyIncome'])
        MonthlyIncome = np.log(MonthlyIncome)

        CustTenure = int(request.form['CustTenure'])

        Designation=request.form['Designation']
        if Designation=='Manager':
                Designation_Manager = 1
                Designation_Executive = 0
                Designation_VP = 0
                Designation_AVP = 0
                Designation_Senior_Manager = 0
        elif Designation=='VP':
                Designation_Manager = 0
                Designation_Executive = 0
                Designation_VP = 1
                Designation_AVP = 0
                Designation_Senior_Manager = 0
        else:
                Designation_Manager = 0
                Designation_Executive = 0
                Designation_VP = 0
                Designation_AVP = 0
                Designation_Senior_Manager = 0

        ExistingPolicyTenure = float(request.form['ExistingPolicyTenure'])
        ExistingPolicyTenure = np.log(ExistingPolicyTenure)

        LastMonthCalls = int(request.form['LastMonthCalls'])
        CustCareScore = float(request.form['CustCareScore'])
        NumberOfPolicy = float(request.form['NumberOfPolicy'])
        
        prediction=model.predict([[SumAssured, Age, MonthlyIncome, CustTenure, Designation_Manager, Designation_VP, ExistingPolicyTenure,
                                    LastMonthCalls, CustCareScore, NumberOfPolicy]])
        output=round(prediction[0],2)
        output = np.exp(output)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry")
        else:
            return render_template('index.html',prediction_text="The agengt bonus can be {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)