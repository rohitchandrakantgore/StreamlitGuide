import streamlit as st
import pandas as pd
import numpy as np


# sidebar() - organize widegets on left panel sidebar

## selectbox() to sidebar
add_selection = st.sidebar.selectbox(
    'select language',
    ['ENGLISH','HINDI','MARATHI']
)

## slider() to sidebar
x = st.sidebar.slider('x')
st.sidebar.write(x, 'squared is' , x*x)


# columns() - place widgets side-by-sdie

left_column, right_column = st.columns(2)
left_column.button("Press Me !!")

with right_column:
    chosen  = st.radio(
        'take one number',
        ("1",'2','3','4','5')
    )
    st.write(f"you have chosen {chosen}")

# expander() - hide large content