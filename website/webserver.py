from flask import Flask
from flask import render_template
from flask import request
import numpy as np
from joblib import load


app = Flask(__name__, template_folder='template')
@app.route('/')
def hello():
    #return "Hello World!"
    return render_template('website.html')
    

@app.route('/result', methods = ['POST', 'GET'])
def result():
    model = load('/website/LR.joblib')
    vals=request.form.to_dict()
    vals1=np.array(list(vals.values()), dtype=float)

    prediction = model.predict(vals1.reshape(1,-1))

    return render_template('website.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


#print(model.predict(6,148,72,35,0,33.6,0.627,50))