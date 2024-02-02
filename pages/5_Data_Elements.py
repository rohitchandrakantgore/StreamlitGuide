import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
import matplotlib.pyplot as plt

st.header(" Data Elements", divider='blue')
st.caption('Usage: this are various methods for displaying various types raw data')

st.subheader(":one: Method Name: :red[dataframe]")
st.text('Syntax : st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, column_order=None, column_config=None)')
st.caption('Usage: Display a dataframe as an interactive table.')
st.caption("works with dataframes from Pandas, PySpark, Snowpark etc and also with types that converted to dataframes e.g. numpy arrays, lists, set and dictionaries.")


st.write("code")
st.code(f"""
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)
""", language='python')
st.write("output")
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)