import pandas as pd
import streamlit as st

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age= st.slider("Select your age",0,100,25)

gender = st.selectbox("Gender",['Male','Female'])

if name:
    st.write(f'Hello {name}')
    st.write(f"Your age is {age}")
    st.write(f"Your gender is {gender}")


data = {
    "Name":['John','Mark','Joy'],
    "Age":[28,39,12],
    "City":['Miami','California','Toronto']
}

df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)


uploaded_file = st.file_uploader("Choose a csv file",type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)