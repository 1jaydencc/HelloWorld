import boto3
import streamlit

image_file = streamlit.file_uploader("Upload an image")

if image_file is not None:
    img = image_file.read()

client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id = streamlit.secrets["aws_access_key_id"], aws_secret_access_key= streamlit.secrets["aws_secret_access_key"])

if streamlit.button('Analyze'):
    with open(img, 'rb') as image_file:
        content = image_file.read()

    response = client.recognize_celebrities(Image = {'Bytes': content}, MaxLabels = 10)

    streamlit.write(response)
