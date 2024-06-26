import streamlit as st 
import google.generativeai as genai
from AppApi import Gemini_api_key

genai.configure(api_key=Gemini_api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]


model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

st.set_page_config(layout="wide")
st.title("🌊 Riding the Wave of AI: Navigating Tomorrow's Technological Frontier 🚀")

# Subheader
st.subheader("Harnessing Artificial Intelligence to Shape a Smarter Future")

# Sidebar
with st.sidebar:
    st.title("Input Your Blog Details")
    st.markdown('Enter Details Of Blog You Want To Generate')
    
    # Input for Blog Title
    blog_title = st.text_input("Blog Title")
    
    # Keywords
    Keywords = st.text_area("Keywords (comma-separated)")
    
    # Number of Words
    numwords = st.slider("Number Of Words", min_value=100, max_value=1500, step=100)
    
    # Submit button
    submitbutton = st.button("Generate Blog")

# Handling the blog generation and display
if submitbutton:
    prompt = f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{Keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {numwords} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."
    
    response = model.generate_content(prompt)
    
    st.write(response.text)
