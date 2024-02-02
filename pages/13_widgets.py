import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Widgets ")
st.sidebar.markdown("# Widgets ")

#slider()
st.write("**slider() widget**")
x = st.slider('x')
st.write(x, 'squared is' , x*x)

st.divider()
st.divider()

# checkbox()
st.write("**checkbox() widget**")
if st.checkbox("Show DataFrame"):
    df4 = pd.DataFrame(
        np.random.randn(10,20),
        columns = ('col %d' % i for i in range(20) )
    )
    st.table(df4)
st.divider()
st.divider()


# selectbox()
st.write("**checkbox() widget**")

df = pd.DataFrame({
        'first_column':[1,2,3,4],
        'second_column':[10,20,30,40]
}
)

option = st.selectbox(
    'select one number', df['first_column']
)

"You Selected ", option

st.divider()
st.divider()


#
st.write("**checkbox() widget**")

st.divider()
st.divider()