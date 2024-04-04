import streamlit as st

import pandas as pd

name= st.text_input("Enter your name here:")
fname =st.text_input("enter your fathers name here:")
adr = st.text_area('Enter your address:')
classdata = st.selectbox("Enter your class :",(1,2,3,4,5,6,))
button =st.button("Done")

if button:
    st.markdown(f"""Name {name}
    Fathers name :{fname} 
    adress {adr}
    classs {classdata}""")


