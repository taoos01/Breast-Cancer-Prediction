import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/Mahdi/OneDrive/Desktop/Projects/BreastCancerData.sav', 'rb'))

input(17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189)

input_as_np_array = np.asarray(input)

reshaped_input = input_as_np_array.reshape(1, -1)

prediction = model.predict(reshaped_input)

if prediction[0] == 0:
    print("Malignant")
else:
    print("Benign")