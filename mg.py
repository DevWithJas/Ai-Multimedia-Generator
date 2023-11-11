import streamlit as st
import openai

# Function to generate images using OpenAI's DALL-E model
def generate_image(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        st.image(image_url, use_column_width=True)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Function to generate text using GPT-3.5-turbo
def generate_text(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                      {"role": "user", "content": prompt}]
        )
        story = response.choices[0].message['content']
        st.text_area("Generated Text", story, height=250)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app layout
st.title("AI multimedia Generator")

# API key input
api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:  # Proceed only if the API key has been entered
    # User prompt input
    prompt = st.text_area("Enter your prompt", height=100)

    # Select service (Image or Text Generation)
    service = st.selectbox("Select Service", ["Image Generation", "Text Generation"])

    if st.button("Generate"):
        if service == "Image Generation":
            generate_image(prompt, api_key)
        elif service == "Text Generation":
            generate_text(prompt, api_key)
else:
    st.warning("Please enter your OpenAI API key to use the app.")
