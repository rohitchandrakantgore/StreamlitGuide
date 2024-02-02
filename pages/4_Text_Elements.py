import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
import matplotlib.pyplot as plt

st.header(" Text Elements", divider='blue')
st.caption('Usage: this are various methods for displaying various types elements specifically')

st.subheader(":one: Method Name: :red[markdown]")
st.text('Syntax : st.markdown(body, unsafe_allow_html=False, *, help=None) ')
st.caption('Usage: string to display as Github-flavored Markdown.')


st.write("code")
st.code(f"""
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
""", language='python')
st.write("output")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)


st.subheader(":two: Method Name: :red[title]")
st.text('Syntax : st.title(body, anchor=None, *, help=None) ')
st.caption('Usage: Display text in title formatting.')

st.write("Code ")
st.code("""
    st.title("Title : ")
    st.title(":blue[_Python_] is really awesome language :100:")
""")

st.write("Result ")
st.title("Title : ")
st.title(":blue[_Python_] is really awesome language :100:")

st.subheader(":three: Method Name: :red[header]")
st.text('Syntax : st.header(body, anchor=None, *, help=None, divider=False) ')
st.caption('Usage: Display text in header formatting.')



st.write("Code ")
st.code("""
    st.header('This is a header with a divider', divider='rainbow')
    st.header('_Streamlit_ is :blue[cool] :sunglasses:')
""")

st.write("Result ")
st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

#####################
st.subheader(":four: Method Name: :red[subheader]")
st.text('Syntax : st.subheader(body, anchor=None, *, help=None, divider=False) ')
st.caption('Usage: Display text in subheader formatting.')



st.write("Code ")
st.code("""
    st.subheader('This is a subheader with a divider', divider='rainbow')
    st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
""")

st.write("Result ")
st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

#####################
st.subheader(":five: Method Name: :red[caption]")
st.text('Syntax : st.caption(body, unsafe_allow_html=False, *, help=None) ')
st.caption('Usage: Display text in small fonts. which can be used for captions, asides, footnotes,sidenotes and other explanatory text')



st.write("Code ")
st.code("""
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
""")

st.write("Result ")
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')


#####################
st.subheader(":six: Method Name: :red[code]")
st.text('Syntax : st.code(body, language="python", line_numbers=False) ')
st.caption('Usage: Display a code block with optional syntax highlighting.')



st.write("Code ")
st.code("""
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
""")

st.write("Result ")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python', line_numbers= True)


#####################
st.subheader(":seven: Method Name: :red[text]")
st.text('Syntax : st.text(body, *, help=None) ')
st.caption('Usage: Write fixed-width and preformatted text.')



st.write("Code ")
st.code("""
st.text('This is some text.')
""")

st.write("Result ")
st.text('This is some text.')

#####################
st.subheader(":eight: Method Name: :red[latex]")
st.text('Syntax : st.latex(body, *, help=None) ')
st.caption('Usage: Display mathematical expressions formatted as LaTeX.')



st.write("Code ")
st.code("""
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
""")

st.write("Result ")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

#####################
st.subheader(":nine: Method Name: :red[divider]")
st.text('Syntax : st.divider() ')
st.caption('Usage: Display a horizontal rule.')



st.write("Code ")
st.code("""
st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule
""")

st.write("Result ")
st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule