import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Mahdi/OneDrive/Desktop/Projects/BreastCancerData.sav', 'rb'))

def breast_cancer(input_data, name):
    input_array = np.asarray(input_data)
    reshaped_array = input_array.reshape(1, -1)
    prediction = loaded_model.predict(reshaped_array)
    if prediction[0] == 0:
        return (f"{name} have Malignant")
    else:
        return (f"{name} have Benign")

def main():
    st.title("Breast Cancer Prediction")

    # "radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"

    name = st.text_input("Enter Patient Name")
    inputs = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]
    
    user_inputs = []

    for feature in inputs:
        value = st.number_input(f"Enter {feature}", value= 0.0, format= '%.4f')
        user_inputs.append(value)

    diagnosis = ''
    if(st.button("Test")):
        result = breast_cancer(user_inputs, name)
        st.success(result)


if __name__ == '__main__':
    main()