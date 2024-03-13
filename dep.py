import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('random_forest_model.pkl','rb'))


# creating a function for Prediction

def pred_rent(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    

    return prediction
  
    
  
def main():
    
    
    # giving a title
    st.title('Rent House prediction')
    
    
    # getting the input data from the user
    
    
    BHK = st.text_input('BHK')
    Size = st.text_input('Size')
    Floor = st.text_input('Floor')
    Area_Type = st.text_input('Area Type')
    Area_Locality = st.text_input('Area Locality')
    City = st.text_input('City')
    Furnishing_Status = st.text_input('Furnishing Status')
    Tenant_Preferred = st.text_input('Tenant Preferred')
    Bathroom = st.text_input('Bathroom')
    Point_of_Contact = st.text_input('Point of Contact')
    
    
    
    # code for Prediction
    pred=''
    
    # creating a button for Prediction
    
    if st.button('resultat'):
        pred = pred_rent([int(BHK), int(Size), int(Floor), int(Area_Type), int(Area_Locality), int(City), int(Furnishing_Status), int(Tenant_Preferred), int(Bathroom), int(Point_of_Contact)])
        
        
    st.success(pred)
    
    
    
    
    
if __name__ == '__main__':
    main()
