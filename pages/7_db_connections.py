import streamlit as st
import pandas as pd
import numpy as np
import time

st.markdown("# DB ")
st.sidebar.markdown("# DB ")

# to manage database secretes in streamlit create a file as  .streamlit/secrets.toml at parent  
# add it in .ignore for better for security 

# connection() - to get data from database

conn = st.connection("my_db")
df = conn.query("select * from student")
st.dataframe(df)

