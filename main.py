import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np



st.title('ứng dụng nhận dạng ảnh chữ số viết tay.')
input = open('lrc_mnist.pkl','rb')
model = pkl.load(input)

st.header('image')
image = st.file_uploader('choose an image:',type=(['png','jpg','jpeg']))


if image is not None:
  image =Image.open(image)
  st.image(image,caption='test image')

  if st.button('Predict'):
    image=image.resize((8*8,1))
    vector =np.array(image)
    label= str((model.predict(vector))[0])

    st.header('ket qua')
    st.text(label)
