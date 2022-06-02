import streamlit as st
import pickle
import numpy as np


# We need code from our notebook
#  we create a function , we copy the code of the saved file in pickle

def load_model():
    with open ("save_steps.pkl", 'rb') as file:
        data = pickle.load(file)
    return data

#  we want to excute the date
data = load_model()

# To access the keys we copy them from notebook
regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

#  Let's  build our streamlit App by creating a function
#  We create streamlit wedgets 

def show_predict_page():
    st.title("Software Developer Salary Prediction")

# we can write text by using a multi line string and we can use a ( .DS_store )(mark down syntex)
#  ( ###  as h3 line ( Like in HTML))
    st.write("""### We need some information to predcit the Salary""")

# If we try to excute the app from the terminal it wont work 
# We need to start it from the main ( app.py ) file.
# Now we need wrtie some code in the (app.py) file. 

