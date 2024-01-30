import streamlit as st
import pandas as pd
import numpy as np


# Writing in Application
# using write() methdd, which takes text,data, matplotblib figures, charts and more .. , streamlit figures it out and render 
st.write("**write() method**")
st.write("This application will cover all the things in streamlit")
st.divider()
st.divider()

# using magic method
st.write("**magic method**")
df = pd.DataFrame({
    'list': list(range(10))
})
df  #interally it takes as st.write(df)
st.divider()
st.divider()

# using st.dataframe() method  - to draw interactive table
st.write("**dataframe() method**")
df2 = np.random.randn(10)
st.dataframe(df2)
st.divider()
## using Pandas Styler object to heightlight some elements from table

df3 = pd.DataFrame(
    np.random.randn(10,20),
    columns = ('col %d' % i for i in range(20) )
)
st.dataframe(df3.style.highlight_max(axis=0))
st.divider()
st.divider()

# using st.table() method - to generate static table
st.write("**table() method**")
df4 = pd.DataFrame(
    np.random.randn(10,20),
    columns = ('col %d' % i for i in range(20) )
)
st.table(df4)

st.divider()
st.divider()

# using line_chart() method - 
st.write("**line_chart() method**")
chart_data = pd.DataFrame(
    np.random.randn(10,3),
    columns = ['a','b','c']
)
st.line_chart(chart_data)

st.divider()
st.divider()

# using map() method - to display daa points on map
st.write("**map() method**")
chart_data = pd.DataFrame(
    np.random.randn(100,2)/ [100,100]+[18.233385,75.694145],
    columns = ['lat','lon']
)
st.map(chart_data)

st.divider()
st.divider()