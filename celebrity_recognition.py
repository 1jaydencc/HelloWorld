import boto3
import streamlit

photo = streamlit.file_uploader("Upload an image")

client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id = streamlit.secrets["aws_access_key_id"], aws_secret_access_key= streamlit.secrets["aws_secret_access_key"])

with open(photo, 'rb') as image:
        response = client.recognize_celebrities(
                {
                   "Image": { 
                      "Bytes": blob,
                      "S3Object": { 
                         "Bucket": "string",
                         "Name": "string",
                         "Version": "string"
                      }
                   }
                })
streamlit.write(response)
