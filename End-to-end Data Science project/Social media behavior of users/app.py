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
        Yearly_avg_view_on_travel_page = float(request.form['Yearly_avg_view_on_travel_page'])
        total_likes_on_outstation_checkin_given = float(request.form['total_likes_on_outstation_checkin_given'])
        total_likes_on_outofstation_checkin_received = float(request.form['total_likes_on_outofstation_checkin_received'])
        week_since_last_outstation_checkin = float(request.form['week_since_last_outstation_checkin'])
        travelling_network_rating = float(request.form['travelling_network_rating'])
        Adult_flag = float(request.form['Adult_flag'])

        preferred_device=request.form['preferred_device']
        if preferred_device=='iOS':
                preferred_device_iOS = 1
                preferred_device_Android = 0
                preferred_device_Laptop = 0
                preferred_device_Mobile = 0
                preferred_device_Tab = 0
                preferred_device_Other = 0
        elif preferred_device=='Mobile':
                preferred_device_iOS = 0
                preferred_device_Android = 0
                preferred_device_Laptop = 0
                preferred_device_Mobile = 1
                preferred_device_Tab = 0
                preferred_device_Other = 0
        elif preferred_device=='Laptop':
                preferred_device_iOS = 0
                preferred_device_Android = 0
                preferred_device_Laptop = 1
                preferred_device_Mobile = 0
                preferred_device_Tab = 0
                preferred_device_Other = 0
        else:
                preferred_device_iOS = 0
                preferred_device_Android = 0
                preferred_device_Laptop = 0
                preferred_device_Mobile = 0
                preferred_device_Tab = 0
                preferred_device_Other = 0

        member_in_family=request.form['member_in_family']
        if member_in_family==3:
                member_in_family_1 = 0
                member_in_family_2 = 0
                member_in_family_3 = 1
                member_in_family_4 = 0
                member_in_family_5 = 0
                member_in_family_10 = 0
        else:
                member_in_family_1 = 0
                member_in_family_2 = 0
                member_in_family_3 = 0
                member_in_family_4 = 0
                member_in_family_5 = 0
                member_in_family_10 = 0

        following_company_page=request.form['following_company_page']
        if following_company_page=='No':
                following_company_page_No = 1
                following_company_page_Yes = 0
        else:
                following_company_page_No = 0
                following_company_page_Yes = 1

        
        prediction=model.predict([[Yearly_avg_view_on_travel_page, total_likes_on_outstation_checkin_given, 
                                    total_likes_on_outofstation_checkin_received, week_since_last_outstation_checkin, travelling_network_rating,
                                    Adult_flag, preferred_device_Laptop, preferred_device_Mobile, preferred_device_iOS, member_in_family_3,
                                    following_company_page_No, following_company_page_Yes]])
        if prediction == 1:
                output = "Yes"
        else:
                output = "No"
        if not output:
            return render_template('index.html',prediction_texts="Sorry")
        else:
            return render_template('index.html',prediction_text="Will user take the product?: {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)