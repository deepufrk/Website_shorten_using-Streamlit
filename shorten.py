import pyshorteners
import streamlit as st
from PIL import Image
st.write("""
# Website Shorten
""")
img = Image.open("short.png")
st.image(img,width=200)
url = st.text_input("Paste the website Link Here",)
submit = st.button('Shorten')

if submit:
	s = pyshorteners.Shortener().tinyurl.short(url)
	st.write(s)

