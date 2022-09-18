import boto3
import streamlit
from io import BytesIO
import json

image_file = streamlit.file_uploader("Upload an image")

if image_file is not None:
    img = image_file.read()
    
file_img = BytesIO(img)

client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id = streamlit.secrets["aws_access_key_id"], aws_secret_access_key= streamlit.secrets["aws_secret_access_key"])

if streamlit.button('Analyze'):
    content=file_img.read()
    response = client.recognize_celebrities(Image = {'Bytes': content})
    json_data = json.load(response)
    name = json_data["CelebrityFaces"][0]["Name"]
    imdb = json_data["CelebrityFaces"][0]["Urls"][1]
    streamlit.write("Name", name)
    streamlit.write()
    streamlit.write("IMDb Profile: [link](imdb)")
    
