import os
import streamlit as st
from dotenv import load_dotenv
from google.genai import Client, types  # Use the newer `google.genai` library now onwards

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon="🤖",  
    layout="centered",
)

# Load API key safely
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")  # Updated variable name for clarity
if not GOOGLE_API_KEY:
    st.error("Missing GEMINI_API_KEY. Check .env file or environment variables.")
    st.stop()

# Initialize Google GenAI client
client = Client(api_key=GOOGLE_API_KEY)

# Verify available models
available_models = [model.name for model in client.models.list()]

# Select the correct model name
MODEL_NAME = "models/gemini-2.0-flash"  # Include the `models/` prefix
if MODEL_NAME not in available_models:
    st.error(f"'{MODEL_NAME}' not found! Available models: {available_models}")
    st.stop()

# Function to generate content using streaming
def generate_response_stream(user_prompt):
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_prompt)],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    # Stream the response
    full_response = ""
    for chunk in client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=contents,
        config=generate_content_config,
    ):
        full_response += chunk.text
        yield chunk.text  # Yield each chunk for streaming
    return full_response

# Initialize chat session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chatbot title
st.title("🤖 Gemini Pro - ChatBot")

# Show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()  # Placeholder for streaming response
        full_response = ""
        try:
            for chunk in generate_response_stream(user_prompt):
                full_response += chunk
                response_placeholder.markdown(full_response)  # Update placeholder with streamed text
        except Exception as e:
            full_response = f"Error: {str(e)}"
            response_placeholder.markdown(full_response)

        # Add assistant message to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": full_response})