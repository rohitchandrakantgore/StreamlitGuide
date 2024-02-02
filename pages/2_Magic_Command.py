import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title(" :red[Magic] Command ")
st.sidebar.title("# Magic Command ")

st.caption('Usage:  it allows us to write almost anything (markdown, data, charts) without having to type an explicit command at all.\
           in the backend it call write() method.')
st.caption('for explicit use , we can change configuration in :blue[~/.streamlit/config.toml] file')

st.write("Use Cases")
code,output = st.columns(2)

with code:
    lines="""
            # Draw a title and some text to the app:
        '''
        # This is the document title

        This is some _markdown_.
        '''

        df = pd.DataFrame({'col1': [1,2,3]})
        df  # 👈 Draw the dataframe

        x = 10
        'x', x  # 👈 Draw the string 'x' and then the value of x

        # Also works with most supported chart types
        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)

        fig  # 👈 Draw a Matplotlib chart
    """
    st.code(lines, language='python')


with output:
    '''
        # This is the document title

        This is some _markdown_.
    '''

    df = pd.DataFrame({'col1': [1,2,3]})
    df  # 👈 Draw the dataframe
    
    x = 10
    'x', x 

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    fig  # 👈 Draw a Matplotlib chart