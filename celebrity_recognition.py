import boto3
import streamlit

image = streamlit.file_uploader("Upload an image")

if image is not None:
    bytes_data=image.getvalue()
    st.write(bytes_data)

client = boto3.client('rekognition', 
                    aws_access_key_id = streamlit.secrets["aws_access_key_id"],
                    aws_secret_access_key= streamlit.secrets["aws_secret_access_key"])

response = client.recognize_celebrities(bytes_data)
streamlit.write(response)
