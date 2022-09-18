import boto3
import streamlit
from io import BytesIO

streamlit.title('Celebrity Recognizer')
streamlit.subheader('By Jayden Cheung')

image_file = streamlit.file_uploader("Upload an image")
streamlit.write("If you get an error, make sure you use a valid JPG or PNG.")

if image_file is not None:
    img = image_file.read()

client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id = streamlit.secrets["aws_access_key_id"], aws_secret_access_key= streamlit.secrets["aws_secret_access_key"])

if streamlit.button('Analyze'):
    file_img = BytesIO(img)
    content=file_img.read()
    response = client.recognize_celebrities(Image = {'Bytes': content})
    if 'Celebrity Faces' in response:
        if 0 in response['CelebrityFaces']:
            if 'Name' in response['CelebrityFaces'][0]:
                streamlit.write("Name:", response['CelebrityFaces'][0]['Name'])
                streamlit.write("IMDb Profile:" , response['CelebrityFaces'][0]['Urls'][1])
    else: 
        streamlit.write("No celebrity")

    
