import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
import style
import openai
from dotenv import load_dotenv
load_dotenv()
import os
from googleapiclient.discovery import build
import pdf_create as pdf
# Set your OpenAI API key and YouTube API key
openai.api_key = os.getenv("OPENAI_API_KEY")
youtube_api_key = os.getenv("YOUTUBE_API_KEY") 

page_bg_img = style.stylespy()  # used for styling the page

# Appname
st.set_page_config(page_title="AI DERMATOLOGIST", layout="wide")

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #fff;'>AI DERMATOLOGIST</h1>", unsafe_allow_html=True)


# Load your model and its weights
model = tf.keras.models.load_model('EfficientNetB2-Skin-87.h5')
class_names = ['Eczema', 'Warts Molluscum and other Viral Infections', 'Melanoma', 'Atopic Dermatitis',
    'Basal Cell Carcinoma (BCC)', 'Melanocytic Nevi (NV)', 'Benign Keratosis-like Lesions (BKL)',
    'Psoriasis pictures Lichen Planus and related diseases', 'Seborrheic Keratoses and other Benign Tumors',
    'Tinea Ringworm Candidiasis and other Fungal Infections']  # List of your class names

# Define the Streamlit app
def main():
    user_input=0
    st.write("Upload an image for classification")
    openai.api_key = "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"
    uploaded_file = 0
    col1,col2=st.columns(2)
    
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        save_path = "uploaded_image.png"
        image.save(save_path)

        st.image(image, caption='Uploaded Image.', use_column_width=True)

        st.write("")
        st.write("Classifying...")

        # Preprocess the image
        image = image.resize((224, 224))
        image = np.array(image)
        image = preprocess_input(image)

        # Make predictions
        predictions = model.predict(np.expand_dims(image, axis=0))

        if np.isnan(predictions).any():
            st.write("Prediction result is NaN. Please try with another image")
        else:
            predicted_class = np.argmax(predictions)
            
            confidence = predictions[0][predicted_class]

            st.write(f"Predicted class: {class_names[predicted_class]}")
            st.write(f"Confidence: {confidence:.2f}")
            #user_input = st.text_input("Describe the patient's condition and symptoms:")
            user_input=class_names[predicted_class]
            #prompt = f"Describe the treatment options for {user_input}. Provide 3 examples, each within 150 words."
            #if st.button("Get Treatment Recommendations"):
                #if prompt:
        # Create a list of message objects as per OpenAI's API requirements
                    # messages = [
                    #{"role": "system", "content": "You are a skin disease diagnosis doctor."},
                    #{"role": "user", "content": prompt}
                    # ]
        
        # Call the OpenAI API for chat completion
                    # response = openai.ChatCompletion.create(
                    #model="gpt-3.5-turbo",
                    # messages=messages
                    #)

        # Extract and display the assistant's response
                    #assistant_response = response['choices'][0]['message']['content']
                    # st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                #else:
                    #st.warning("Please describe the patient's condition and symptoms.")
    st.title("AI DOCTOR")

    input_choice = st.radio("Select Input Type", ["Select questions", "write your own question"])
    p_prompt = ""

    if input_choice == "Select questions":
        dropdown_choice = st.selectbox("Select promopt", [
            "When to see a doctor?",
            "Causes of the disease",
            "Symptoms of the disease",
            "Diagnosis of the disease",
            "Treatment of the disease",
            "Prevention of the disease",
        ])
        p_prompt = dropdown_choice
        st.write("Selected:", dropdown_choice)
    else:
        text_input = st.text_input("Enter your question here")
        p_prompt = text_input
        st.write("Entered:", text_input) 
    if p_prompt:
        if p_prompt:
            messages = [
                {"role": "system", "content": "You are a skin disease diagnosis doctor. You have diagnosed "+str(user_input)},
                {"role": "user", "content": p_prompt}
            ]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            assistant_response = response['choices'][0]['message']['content']
            st.write("Skin Disease Diagnosis Doctor:", assistant_response)
        else:
            st.warning("Please describe the patient's condition and symptoms.")                       
    st.title("Treatment Recommendations")
    # Add YouTube video search functionality
    st.write("\n")
    st.header("Search for Disease Treatment Videos on YouTube")
    disease_to_search = user_input
    if st.button("Search on YouTube"):
        if disease_to_search:
            # Initialize the YouTube Data API client
            youtube = build('youtube', 'v3', developerKey=youtube_api_key)

            # Perform the YouTube search
            search_response = youtube.search().list(
                q=f"{disease_to_search} treatment",
                part="id,snippet",
                type="video",
                maxResults=5  # You can adjust the number of results here
            ).execute()

            # Display the search results as clickable links
            st.write(f"Search results for '{disease_to_search} treatment' on YouTube:")
            for search_result in search_response.get("items", []):
                video_id = search_result["id"]["videoId"]
                video_title = search_result["snippet"]["title"]
                st.markdown(f"- [{video_title}](https://www.youtube.com/watch?v={video_id})")

            # Display video search results with thumbnails
            st.header("YouTube Video Search Results")

            for search_result in search_response.get("items", []):
                video_title = search_result["snippet"]["title"]
                video_description = search_result["snippet"]["description"]
                video_id = search_result["id"]["videoId"]
                video_thumbnail_url = search_result["snippet"]["thumbnails"]["medium"]["url"]  # Use "medium" format

                # Create a hyperlink around the thumbnail image
                video_link = f"[![{video_title}]({video_thumbnail_url})](https://www.youtube.com/watch?v={video_id})"
                st.markdown(video_link, unsafe_allow_html=True)
                st.write(f"Title: {video_title}")
                st.write(f"Description: {video_description}")
                st.write(f"Video ID: {video_id}")
        else:
            st.warning("Please enter a disease name to search for treatment videos on YouTube.")

    st.title("PDF of the report")
    if st.button("Generate PDF"):
        link = pdf.create_qr_code_pdf(user_input,assistant_response,p_prompt)
         
        st.write("[Click to view pdf](%s)" % link)
    
    items = [
    '1. Eczema',
    
    '2. Melanoma',
    '3. Atopic Dermatitis',
    '4. Basal Cell Carcinoma (BCC)',
    '5. Melanocytic Nevi (NV)',
    '6. Benign Keratosis-like Lesions (BKL)',
    '7. Psoriasis pictures Lichen Planus and related diseases',
    '8. Seborrheic Keratoses and other Benign Tumors',
    '9. Tinea Ringworm Candidiasis and other Fungal Infections',
    '10. Warts Molluscum and other Viral Infections'
]

    st.title("About this model")
    st.subheader("This model is capable of classifying:")
    for item in items:
        st.write("- " + item)
    
        
# Run the app
if __name__ == '__main__':
    main()
