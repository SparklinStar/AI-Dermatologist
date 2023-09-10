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

page_bg_img = style.stylespy()  # used for styling the page

# Appname
st.set_page_config(page_title="Skin Disease Classifier", layout="wide")

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #fff;'>Skin Disease Classifier</h1>", unsafe_allow_html=True)


# Load your model and its weights
model = tf.keras.models.load_model('EfficientNetB2-Skin-87.h5')
class_names = ['Eczema', 'Warts Molluscum and other Viral Infections', 'Melanoma', 'Atopic Dermatitis',
    'Basal Cell Carcinoma (BCC)', 'Melanocytic Nevi (NV)', 'Benign Keratosis-like Lesions (BKL)',
    'Psoriasis pictures Lichen Planus and related diseases', 'Seborrheic Keratoses and other Benign Tumors',
    'Tinea Ringworm Candidiasis and other Fungal Infections']  # List of your class names

# Define the Streamlit app
def main():
    st.write("Upload an image for classification")
    openai.api_key = "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"
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
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
            
            prompt2 = f"Describe when to see doctor for {user_input} within 150 words."
            if st.button("When to see a doctor?"):
                if prompt2:
                    messages = [
                    {"role": "system", "content": "You are a skin disease diagnosis doctor."},
                    {"role": "user", "content": prompt2}
                    ]
                    
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                else:
                    st.warning("Please describe the patient's condition and symptoms.")
            prompt3 = f"Describe the causes of {user_input} within 150 words."
            if st.button("Causes of the disease?"):
                if prompt3:
                    messages = [
                    {"role": "system", "content": "You are a skin disease diagnosis doctor."},
                    {"role": "user", "content": prompt3}
                    ]
                    
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                else:
                    st.warning("Please describe the patient's condition and symptoms.")
            prompt4 = f"Describe the symptoms of {user_input} within 150 words."
            if st.button("Symptoms of the disease?"):
                if prompt4:
                    messages = [
                    {"role": "system", "content": "You are a skin disease diagnosis doctor."},
                    {"role": "user", "content": prompt4}
                    ]
                    
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                else:
                    st.warning("Please describe the patient's condition and symptoms.")
            prompt5 = f"Describe the diagnosis of {user_input} within 150 words."
            if st.button("Diagnosis of the disease?"):
                if prompt5:
                    messages = [
                    {"role": "system", "content": "You are a skin disease diagnosis doctor."},
                    {"role": "user", "content": prompt5}
                    ]
                    
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                else:
                    st.warning("Please describe the patient's condition and symptoms.")
            prompt6 = f"Describe the treatment of {user_input} within 150 words."
            if st.button("Treatment of the disease?"):
                if prompt6:
                    messages = [
                    {"role": "system", "content": "You are a skin disease diagnosis doctor."},
                    {"role": "user", "content": prompt6}
                    ]
                    
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                else:
                    st.warning("Please describe the patient's condition and symptoms.")
            prompt7 = f"Describe the prevention of {user_input} within 150 words."
            if st.button("Prevention of the disease?"):
                if prompt7:
                    messages = [
                    {"role": "system", "content": "You are a skin disease diagnosis doctor."},
                    {"role": "user", "content": prompt7}
                    ]
                    
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                else:
                    st.warning("Please describe the patient's condition and symptoms.")
            prompt8 = f"Describe the complications of {user_input} within 150 words."
            if st.button("Complications of the disease?"):
                if prompt8:
                    messages = [
                    {"role": "system", "content": f"You are a skin disease diagnosis doctor."},
                    {"role": "user", "content": prompt8}
                    ]
                    
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                else:
                    st.warning("Please describe the patient's condition and symptoms.")
            prompt9 = st.text_input('Anything you want to ask about the disease?','')
            #prompt9 = f"Describe the risk factors of {user_input} within 150 words."
            if st.button("Click to ask the doctor"):
                if prompt9:
                    messages = [
                    {"role": "system", "content": f"You are a skin disease diagnosis doctor.You have diagnosed {user_input}"},
                    {"role": "user", "content": prompt9}
                    ]
                    
                    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                    )
                    assistant_response = response['choices'][0]['message']['content']
                    st.write("Skin Disease Diagnosis Doctor:", assistant_response)
                else:
                    st.warning("Please describe the patient's condition and symptoms.")        
                    

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


    st.title("This model is capable of classifying:")
    for item in items:
        st.write("- " + item)
        
# Run the app
if __name__ == '__main__':
    main()
