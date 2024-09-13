import streamlit as st
import requests

st.title("LinkedIn PDF to HTML Resume Generator")

# Create an input field for the OpenAI API key
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password",
                               help="Enter the OpenAI API key securely here")

# Create a file uploader to upload the LinkedIn PDF
uploaded_file = st.file_uploader("Upload your LinkedIn PDF", type=["pdf"])

# Process the PDF and API key when both are provided
if openai_api_key and uploaded_file is not None:
    st.write("Processing your LinkedIn PDF...")

    # Prepare the files and data to be sent to FastAPI
    files = {"pdf": uploaded_file.getvalue()}
    data = {"openai_api_key": openai_api_key}

    try:
        response = requests.post("https://resume-project-backend.onrender.com/pdf_router/generate-html/", files=files, data=data)

        if response.status_code == 200:
            # Parse the HTML resume from the response
            html_resume = response.json().get("html_resume")

            st.components.v1.html(html_resume, height=800, scrolling=True)

            # Display the generated HTML resume
            # st.markdown(html_resume, unsafe_allow_html=True)

            # Provide a download button for the HTML resume
            st.download_button("Download HTML Resume", html_resume, file_name="resume.html")

            st.markdown("This is developed by Sonu(sonuiiitian@gmail.com using streamlit and FastAPI")

        else:
            st.error("Failed to generate resume. Please check the OpenAI API key and try again.")

    except Exception as e:
        st.error(f"Error occurred: {e}")
