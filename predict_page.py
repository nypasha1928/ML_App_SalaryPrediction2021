import streamlit as st
import pickle
import numpy as np


# We need code from our notebook
#  we create a function , we copy the code of the saved file in pickle

def load_model():
    with open ("saved_steps.pkl", 'rb') as file:
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

# Now we need to add the Tuple select boxes for the Country
    countries = {
        "United States",
        "India",
        "Germany",
        "United Kingdom",
        "Canada",
        "France",
        "Brazil",
        "Spain",
        "Netherlands",
        "Australia",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
        "Turkey",
        "Switzerland",
        "Israel",
        "Norway",
        }

# We need to add a Tuple select box for the Education
    education = {
        "Less than a Bachelors",
        "Bachelor's degree",
        "Master's degree",
        "Post grad"
    } 
# Create a select box 
    country = st.selectbox("Country" , countries)
    education = st.selectbox("Education Level" , education )

# create a slider for years of experiance , give a min value, max value and a default.
    experiance =  st.slider("Years of Experiance", 0, 50, 3)

#  Add a button to  start prediction and asign it to a variable 
#  This means that if we click on the button = True, if we dont click on the button = False
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experiance ]])
        X[:, 0] = le_country.fit_transform(X[:,0])
        X[:, 1] = le_education.fit_transform(X[:,1])    
        X = X.astype(float)

        salary= regressor.predict(X)

# Display , {} it is an array , [0] we want to access the first value, :.2f Two decimal values.
        st.subheader(f"The estimated salary is ${salary[0]:.02f}") 


#  Results : Now we need to add a side bar :- The app.py page.
# And  a second page     