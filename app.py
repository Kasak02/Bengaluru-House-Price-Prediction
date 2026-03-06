import streamlit as st
import pickle
import pandas as pd

st.title("Bengaluru House Prediction")

house = pickle.load(open('Cleaned_data.pkl','rb'))
linear_reg =pickle.load(open('linear_reg.pkl','rb'))

loc = [col.replace("location_","") for col in linear_reg.feature_names_in_ if "location_" in col]
location =st.selectbox("Location",loc)

BHK = st.slider("BHK", 1,20)
bath = st.slider("Enter No of Bathrooms" , 1,15)
balcony = st.slider("Enter No of Balconies" , 0,3)
total_sqft = st.number_input("Enter total square feet",min_value=300.0 , max_value=30000.0)

def predict_price(location,total_sqft,bath,balcony,BHK):
    input = pd.DataFrame(columns=linear_reg.feature_names_in_)
    input.loc[0]=0

    input['total_sqft'] =total_sqft
    input['bath'] = bath
    input['balcony']=balcony
    input['BHK'] = BHK

    loc_col = "location_"+ location

    if loc_col in input.columns:
        input[loc_col] = 1

    prediction = linear_reg.predict(input)
    return prediction[0]

if st.button("Predict Price"):
    price = predict_price(location,total_sqft,bath,balcony,BHK)
    st.success(f"Estimated House Price:  ₹ {round(price,2)} Lakhs")





