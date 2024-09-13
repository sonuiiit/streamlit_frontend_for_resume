What is in the project:-

Deployed frontend:- https://appfrontendforresume-x9ezokyz82kggtyn8sjnzq.streamlit.app/

---

# LinkedIn PDF to HTML Resume Generator

This project features a **Streamlit** frontend and a **FastAPI** backend to convert a LinkedIn PDF resume into an HTML format. The HTML resume is displayed directly within the Streamlit application.

## Overview

- **Frontend**: Streamlit app that allows users to upload a LinkedIn PDF and enter an OpenAI API key. Displays the generated HTML resume within the app.
- **Backend**: FastAPI service that processes the PDF, generates the HTML resume using OpenAI, and returns the HTML content.

## Setup

### Prerequisites

- Python 3.7+
- FastAPI
- Streamlit
- OpenAI Python client
- PyPDF2