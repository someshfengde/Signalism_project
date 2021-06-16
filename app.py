import streamlit as st
import functions as fn
import numpy as np
import pandas as pd

st.title('Text poetry generator')

st.write('enter the text data to get our model started ')

scentence = st.text_input('Input your text here')

if scentence:
    predictions = fn.get_prediction(scentence)
else:
    st.write('enter the valid text input')

st.write(predictions)




