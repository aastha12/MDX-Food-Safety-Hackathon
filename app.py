#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import preprocessing


app = Flask(__name__)
model = pickle.load(open('MDX Hackathon.pkl','rb'))


@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    final_features = preprocessing.StandardScaler().fit(final_features).transform(final_features)
    prediction = model.predict(final_features)
    proba_prediction = model.predict_proba(final_features)
    print(prediction[0],proba_prediction[0][1])

    #output = round(prediction[0], 2)
    if(prediction[0]==0):
        text="The case will not be an alert case. The probability of it being an alert case is {}%.".format((proba_prediction[0][1])*100)
    elif(prediction[0]==1):
        text="The case will be an alert case. The probability of it being an alert case is {}%.".format((proba_prediction[0][1])*100)
        
    return render_template('home.html', prediction_text=text)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)



if __name__ == '__main__':
    app.run(debug=False)


# In[ ]:





# In[ ]:




