"""
This app is a simple UI to infer Helmet Detection YOLOv10 model with Streamlit
"""

import streamlit as st
from helmet_model import HelmetModel

from PIL import Image

# Load the model
model = HelmetModel('best.pt')

st.title('Helmet Detection YOLOv10')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    results = model.predict(image)
    st.image(results[0].save('./results/result.jpg'), caption='Helmet Detection', use_column_width=True)