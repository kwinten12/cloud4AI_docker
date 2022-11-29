import pandas as pd 
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('diabetes.csv')

y = df['Outcome'].values
x = df.drop(['Outcome','Insulin','BMI','DiabetesPedigreeFunction'],axis=1).values
x_train = x[:-100]
y_train = y[:-100]
x_test = x[-100:]
y_test = y[-100:]

LR = LogisticRegression()
LR.fit(x_train, y_train)

# Save model
from joblib import dump
dump(LR, '/model/LR.joblib') 