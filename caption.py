import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def query(uploaded_file):
    # Read the file directly using the UploadedFile object
    data = uploaded_file.read()
    
    # Send the file data to the API
    response = requests.post(API_URL, headers=headers, data=data)
    
    # Return the JSON response from the API
    return response.json()

# Streamlit file uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if a file has been uploaded
if uploaded_file is not None:
    if st.button("Generate Caption"):
        # Call the query function with the uploaded file
        output = query(uploaded_file)
        
        # Display the output
        st.write(output)
else:
    st.write("Please upload an image.")


import base64

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("D:\Screenshots\pro.png")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)
