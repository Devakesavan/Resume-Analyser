import streamlit as st
import fitz
import re
import constant
from constant import *
import json

# Add custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #1e1e1e;
    }
    .stFileUploader label {
        color: #00bcd4;
        font-size: 1.1rem;
        font-weight: bold;
    }
    .stTextInput div {
        border-color: #00bcd4;
    }
    .stTextInput input {
        padding: 10px;
        font-size: 1rem;
        background-color: #2d2d2d;
        color: #ffffff;
        border-radius: 5px;
        border: 1px solid #00bcd4;
    }
    .stButton button {
        background-color: #00bcd4;
        color: white;
        font-size: 1rem;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color: #0097a7;
    }
    .stExpander {
        background-color: #2d2d2d;
        border-radius: 8px;
        margin-top: 20px;
    }
    .stExpander header {
        background-color: #00bcd4;
        color: white;
        font-size: 1.1rem;
        border-radius: 8px 8px 0 0;
    }
    .stExpander div {
        background-color: #2d2d2d;
        padding: 20px;
    }
    .stMarkdown h1 {
        font-size: 2.5rem;
        color: #00bcd4;
        text-align: center;
    }
    .stMarkdown h2 {
        font-size: 1.5rem;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to read PDF file
def read_pdf_file(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text
def authenticate(username, password):
    # Implement authentication logic here
    # Check if username and password are valid
    return True  # For demonstration purposes, always return True

def main():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful! Redirecting to the main page...")
            # Redirect to main page or load Streamlit app here
            # You can use st.experimental_set_query_params to pass session information
        else:
            st.error("Invalid username or password. Please try again.")

# Function to interact with the Generative AI model
def Model(data, user_prompt):
    import google.generativeai as genai

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Requesting response in JSON format
    prompt = "{}\n{} Please provide the response in JSON format.".format(data, user_prompt)
    response = model.generate_content(prompt)

    # Remove unwanted formatting
    response_text = response.text.strip()
    if response_text.startswith("") and response_text.endswith(""):
        response_text = response_text[3:-3].strip()
    if response_text.startswith("json\n"):
        response_text = response_text[5:].strip()

    # Try to parse the response as JSON
    try:
        response_json = json.loads(response_text)
    except json.JSONDecodeError:
        # If JSON parsing fails, return error message and original response text
        response_json = {"error": "Failed to parse response as JSON", "response": response_text}

    return response_json, response_text

# Function to save the parsed data to a JSON file
def save_to_json(parsed_data, file_name="parsed_resume_data.json"):
    with open(file_name, 'w') as json_file:
        json.dump(parsed_data, json_file, indent=4)
    return file_name

# Streamlit interface
st.markdown("<h1>Resume Parsing with Streamlit</h1>", unsafe_allow_html=True)
st.write("Upload a PDF file and provide a prompt to interact with the Generative AI model.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file
    file_path = uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Read and process the PDF file
    resume_text = read_pdf_file(file_path)
    
    if resume_text:
        st.markdown("<h2>Provide Your Prompt</h2>", unsafe_allow_html=True)
        user_prompt = st.text_input("Please provide your prompt for the model:")

        if st.button("Submit Prompt"):
            content, raw_text = Model(resume_text, user_prompt)
            
            # Display the prompt output text
            st.markdown("<h2>Prompt Output</h2>", unsafe_allow_html=True)
            st.write(raw_text)

            json_path = save_to_json(content, "prompt_output.json")
            with open(json_path, "rb") as f:
                st.download_button(
                    label="Download Prompt Output as JSON",
                    data=f,
                    file_name="prompt_output.json",
                    mime="application/json"
                )
            
            # Option for further interaction
            st.markdown("<h2>Further Interaction</h2>", unsafe_allow_html=True)
            further_prompt = st.text_input("Would you like to ask something else?")
            if st.button("Submit Further Prompt"):
                further_content, further_raw_text = Model(resume_text, further_prompt)
                
                # Display the further prompt output text
                st.markdown("<h2>Further Prompt Output</h2>", unsafe_allow_html=True)
                st.write(further_raw_text)

                further_json_path = save_to_json(further_content, "further_prompt_output.json")
                with open(further_json_path, "rb") as f:
                    st.download_button(
                        label="Download Further Prompt Output as JSON",
                        data=f,
                        file_name="further_prompt_output.json",
                        mime="application/json"
                    )