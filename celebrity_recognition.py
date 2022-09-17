image = streamlit.file.uploader() 

client = boto3.client('rekognition', 
                    aws_access_key_id = "AKIA3UTMBR4M67BK55G4",
                    aws_secret_access_key= "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")

with open(image, 'rb') as source_image:
    source_bytes=source_image.read()

response = client.recognize_celebrities(source_image)
streamlit.write(response['Name'])
