import boto3
import streamlit

photo = streamlit.file_uploader("Upload an image")

client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id = streamlit.secrets["aws_access_key_id"], aws_secret_access_key= streamlit.secrets["aws_secret_access_key"])

response = client.recognize_celebrities(Image = {'Bytes': photo})

streamlit.write(response)
