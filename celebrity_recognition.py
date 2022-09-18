import boto3
import streamlit
from io import BytesIO

image_file = streamlit.file_uploader("Upload an image")
streamlit.write("If you get an error, you either didn't use a JPG or PNG, the image is invalid, or the image does not contain a celebrity face. I know, it's a work in progress.")

if image_file is not None:
    img = image_file.read()

client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id = streamlit.secrets["aws_access_key_id"], aws_secret_access_key= streamlit.secrets["aws_secret_access_key"])

if streamlit.button('Analyze'):
    file_img = BytesIO(img)
    content=file_img.read()
    response = client.recognize_celebrities(Image = {'Bytes': content})
    if 'Name' in response['CelebrityFaces'][0]:
        streamlit.write("Name:", response['CelebrityFaces'][0]['Name'])
        streamlit.write("IMDb Profile:" , response['CelebrityFaces'][0]['Urls'][1])
    else: 
        streamlit.write("No celebrity")

    
