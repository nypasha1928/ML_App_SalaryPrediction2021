import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#  we need to clean the data, copy the code from salary predcition page
def shorten_categories (categories , cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i]>= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'other'
    return categorical_map


def clean_experience(x):
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if "Bachelor's degree" in x:
        return "Bachelor's degree"
    if "Master's degree" in x:
        return "Master's degree"
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


# Note : In order not to run this step again when we refresh the pag
#  we can use a technique in streamlit ( cache)
@st.cache

#  we need a function to load the data       
def load_data():
    df = pd.read_csv("DATA/survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    
    df = df[df["ConvertedCompYearly"].notnull()]
    df= df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment" , axis=1)
    
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df['ConvertedCompYearly'] <= 25000]
    df = df[df['ConvertedCompYearly'] >= 10000]
    df = df[df['Country'] != 'other']

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)

    return df

# Execute data
df = load_data()

#  Display the page , we create a function
def show_explore_page():
    st.title("Explore Software Enginerr Salaries")

    st.write("""### Stack Overflow Developer Survey 2021""")

#  We need to explore three different charts.
    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )  

#  Go to app.py page to import the explore page by writing a code 

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)