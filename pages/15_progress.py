import streamlit as st
import pandas as pd
import numpy as np
import time


st.markdown("# Progress ")
st.sidebar.markdown("# Progress ")

"Starting a huge computation ..."

# placeholder

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

"... Done"
