# AI DERMATOLOGIST

AI DERMATOLOGIST is a powerful web application designed to revolutionize dermatological diagnosis and patient interaction. This app combines cutting-edge technologies such as image recognition, natural language processing (NLP), and external APIs to provide a comprehensive and user-friendly experience.

![AI DERMATOLOGIST](https://www.youtube.com/watch?v=eJbUr5cVQB4)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Introduction
AI DERMATOLOGIST aims to make dermatological healthcare more accessible and informative. It leverages AI to classify skin conditions, offers expert consultation through OpenAI's GPT-3.5, scrapes relevant YouTube videos for education, and generates PDF reports based on interactions. With a user-friendly interface, this app provides an efficient and effective solution for both patients and healthcare professionals.

## Features
### 1. Skin Condition Classification
- Upload images for rapid and accurate classification of skin conditions.
- Utilizes a trained model based on EfficientNetB2 architecture.
- Displays the predicted class and confidence level.

### 2. Expert Consultation
- Users can ask questions about their skin condition, symptoms, or treatment options.
- OpenAI's GPT-3.5 provides personalized responses and expert insights.

### 3. YouTube Video Recommendations
- Search for disease-specific treatment and information videos on YouTube.
- Enhance patient education with curated video content.

### 4. PDF Report Generation
- Generate PDF reports summarizing interactions with the AI.
- A valuable resource for discussions with healthcare professionals.

### 5. Privacy and Security
- Ensures the privacy and security of user data.
- Maintains confidentiality in all interactions.

## Setup
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your OpenAI and YouTube API keys in the `.env` file.

```python
# .env
OPENAI_API_KEY=your_openai_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

## Usage
1. Run the Streamlit app using `streamlit run app.py`.
2. Upload an image for classification.
3. Ask questions related to the skin condition.
4. Explore YouTube videos for educational purposes.
5. Generate PDF reports based on interactions.

## License
This project is licensed under the [MIT License](LICENSE).

AI DERMATOLOGIST is a significant step forward in dermatological healthcare, offering accessibility, convenience, and valuable insights for users. Feel free to contribute and improve this project further.
