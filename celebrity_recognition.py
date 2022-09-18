import boto3
import streamlit

image = streamlit.file_uploader("Upload an image")

client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id = streamlit.secrets["aws_access_key_id"], aws_secret_access_key= streamlit.secrets["aws_secret_access_key"])

if st.button('Analyze'):
    with open(image, 'rb') as image_file:
        content = image_file.read()

    response = client.recognize_celebrities(Image = {'Bytes': content}, MaxLabels = 10)

    streamlit.write(response)
