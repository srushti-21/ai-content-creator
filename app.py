# app.py

import streamlit as st
from dotenv import load_dotenv
import os
from chain import create_blog_chain, create_youtube_title_chain # import both functions

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(layout="wide", page_title="AI Content Creator")

st.markdown("""
    <style>
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Initialize the chain ---

# Create the chain once and store it in session state to avoid re-creating it on every script rerun.
if 'blog_chain' not in st.session_state:
    st.session_state.blog_chain = create_blog_chain(groq_api_key)
if 'youtube_chain' not in st.session_state:
    st.session_state.youtube_chain = create_youtube_title_chain(groq_api_key)
    
    
# --- Streamlit App UI ---

st.title("AI Content Creator")

# Dropdown to select cotent type
content_type = st.selectbox(
    "Choose the type of content to generate:",
    ("Blog Post", "YouTube Video Titles")
)

# Input from user
user_topic = st.text_input("Enter the topic:")

# Button to trigger generation
if st.button("Generate Content"):
    if user_topic:
        if content_type == "Blog Post":
            with st.spinner("Generating your blog post... please wait."):
                # Run the chain with user's topic
                response = st.session_state.blog_chain.invoke({"topic": user_topic})
                # Display result
                st.subheader("Your Generated Blog Post:")
                st.markdown(response['text'])
        elif content_type == "YouTube Video Titles":
            with st.spinner("Generating YouTube titles... please wait."):
                # The 'text' key now contains python list!
                response_list = st.session_state.youtube_chain.invoke({"topic": user_topic})['text']
                st.subheader("Your Generated YouTube Titles:")
                # Display list
                for title in response_list:
                    st.write(title)
    else:
        st.warning("Please enter a topic first.")