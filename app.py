import streamlit as st

# imort the function from the page  
from predict_page import show_predict_page
from explore_page import show_explore_page

#  Add a selection box and put it in a side bar
#  for the explore page , we need to put this slider bar in a variable (page)
page = st.sidebar.selectbox("Explore or Predict",("Predict", "Explore"))

#  then we write a condiction
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()    

    
# Now we need to implement the explore page


# # Execute the function
# show_predict_page()

# Quick the server by pressing (Control C)