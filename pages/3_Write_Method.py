import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
import matplotlib.pyplot as plt

st.sidebar.title("Write Method ")

st.header(" Method Name: :red[Write]", divider=True)
st.text('Syntax : st.write(*args, unsafe_allow_html=False, **kwargs)')
st.caption('Usage: it return the objects, strings, text , maps, dataframes etc. ')

st.write("Use Cases")

use1,use2,use3,use4 = st.columns(4)

with use1:
    1 ,'Text / String'
    st.caption("prints formatted string with emojies, colored text, latex experssion etc.")
    st.write('Hello, *Everyone!* :sunglasses:')
    st.write('1 + 1 = ', 2)

with use2:
    2 , 'DataFrame'
    st.caption("prints dataframes as table")
    df = pd.DataFrame({
    'numbers': list(range(10))
    })
    st.write(df)

with use3:
    3, "Error"
    st.caption("prints exception")
    try:
        div = 0/0
    except Exception as error:
        st.write(error)

with use4:
    4, "Functions/ Classes"
    st.caption("Prints info about function or class")
    st.write(time.ctime())



use5,use6,use7 = st.columns(3)
with use5:
    5,"Module"
    st.caption("Prints info about module")
    st.write(pd.api)
with use6:
    6, "Dictionary"
    st.caption("prints dictionary in interactive widget")
    dict_ex = {k:k**2 for k in range(10)}
    st.write(dict_ex)

with use7:
    7, "Matplotlib Figures"
    st.caption("prints matplotlib figures")
    fig, ax = plt.subplots()
    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')
    st.write(fig)







