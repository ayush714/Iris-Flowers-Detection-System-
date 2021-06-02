import numpy as np 
import joblib 


def preprocessdata(sepal_length, sepal_width, petal_length, petal_width):
    test_data = [[sepal_length, sepal_width, petal_length, petal_width] ]
    trained_model = joblib.load("model.pkl") 
    prediction = trained_model.predict(test_data) 

    return prediction 
