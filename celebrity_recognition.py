import boto3
import streamlit as st
from io import BytesIO

st.title('Celebrity Recognizer')
st.subheader('By Jayden Cheung')
st.write("The celebrity recognizer will recognize any celebrity from an image as long as their face is prominent. Just upload an image and we'll do the rest")

image_file = st.file_uploader("Upload an image")
st.write("Make sure you use a valid JPG or PNG. Other image types will give you an error.")

if image_file is not None:
    img = image_file.read()

client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id = st.secrets["aws_access_key_id"], aws_secret_access_key= st.secrets["aws_secret_access_key"])

if st.button('Analyze'):
    file_img = BytesIO(img)
    content=file_img.read()
    response = client.recognize_celebrities(Image = {'Bytes': content})
    if 'Celebrity Faces' in response:
        if 0 in response['CelebrityFaces']:
            if 'Name' in response['CelebrityFaces'][0]:
                st.write("Name:", response['CelebrityFaces'][0]['Name'])
                st.write("IMDb Profile:" , response['CelebrityFaces'][0]['Urls'][1])
    else: 
        st.write("No celebrity")

    
