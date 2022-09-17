image = streamlit.file.uploader("Upload an image")

if image is not None:
    bytes_data=image.getvalue()
    st.write(bytes_data)

client = boto3.client('rekognition', 
                    aws_access_key_id = "AKIA3UTMBR4M67BK55G4",
                    aws_secret_access_key= "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")

with open(image, 'rb') as source_image:
    source_bytes=source_image.read()

response = client.recognize_celebrities(bytes_data)
streamlit.write(response['Name'])
