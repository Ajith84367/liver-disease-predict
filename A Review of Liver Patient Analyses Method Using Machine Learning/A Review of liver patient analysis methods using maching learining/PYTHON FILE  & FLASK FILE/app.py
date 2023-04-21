# import required lib
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn


app = Flask(__name__)

model = pickle.load(open('drug_rf.pkl', 'rb'))


@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/getdata', methods=['POST'])
def pred():
    age = request.form['Age']
    print(age)
    gender = request.form['Gender']
    print(age, gender)
    total_bilirubin = request.form['Total_Bilirubin']
    print(age, gender, total_bilirubin)
    direct_bilirubin = request.form['Direct_Bilirubin']
    print(age, gender, total_bilirubin, direct_bilirubin)
    alkaline_phosphotase = request.form['Alkaline_Phosphotase']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase)
    alamine_aminotransferase = request.form['Alamine_Aminotransferase']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase)
    aspartate_aminotransferase = request.form['Aspartate_Aminotransferase']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
          aspartate_aminotransferase)
    total_proteins = request.form['Total_Proteins']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
          aspartate_aminotransferase, total_proteins)
    albumin = request.form['Albumin']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
          aspartate_aminotransferase, total_proteins, albumin)
    albumin_and_globulin_ratio = request.form['Albumin_and_Globulin_Ratio']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
          aspartate_aminotransferase, total_proteins, albumin, albumin_and_globulin_ratio)

    inp_features = [[int(age), int(gender), np.log(float(total_bilirubin)), np.log(float(direct_bilirubin)),
                     int(alkaline_phosphotase), int(alamine_aminotransferase), int(aspartate_aminotransferase),
                     np.log(float(total_proteins)),
                     np.log(float(albumin)), np.log(float(albumin_and_globulin_ratio))]]
    print(inp_features)
    prediction = model.predict(inp_features)
    print(type(prediction))
    t = prediction[0]
    print(t)
    if t > 0.5:
        prediction_text = 'You have a Liver disease, Please consult a Doctor'
        else:
            prediction_text='Congratualation you dont have liver disease
            print(prediction_text)
            return render_template('submit.html', prediction_results=prediction_text)
        
 if __name__ =="__main__":
    app.run()

