import fitz
from transformers import pipeline
from huggingface_hub import login

# Load a summarization model using Hugging Face's Inference API
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Authenticate with hugging face token
token = "YOUR_TOKEN_HERE"
login(token=token)

try:
    # Opening pdf file using PyMuPDF
    doc = fitz.open("Certificate of Matriculation.pdf")
    ARTICLE = ""
    for page in doc:
        text = page.get_text()
        ARTICLE += text

    # Using the summariser to generate a summary and print it out
    print(summarizer(ARTICLE, max_length=100, min_length=30, do_sample=False))
except FileNotFoundError:
    print("Error: PDF file not found.")
except Exception as e:
    print(f"An error occurred: {e}")