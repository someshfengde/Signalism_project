import streamlit as st
import functions as fn

st.title('Text poetry generator')

st.write('enter the text data to get our model started ')

scentence = st.text_input('Input your text here')

if scentence:
    st.title('Cooking some stuff')
    predictions = fn.get_prediction(scentence)
    st.write(predictions)
else:
    st.write('enter the valid text input')








