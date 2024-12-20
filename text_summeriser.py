from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from transformers import pipeline
from huggingface_hub import login
from jinja2 import Environment, FileSystemLoader
import fitz

app =FastAPI()


# Load a summarization model using Hugging Face's Inference API
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Authenticate with hugging face token
token = "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"
login(token=token)

# Create a Jinja2 environment to render HTML templates
env = Environment(loader=FileSystemLoader("."))

# Serve static files
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
def read_root():
    return RedirectResponse(url="/summarize", status_code=302)
@app.get("/summarize")
def summarize_get():
    return {"message": "Please use the POST endpoint to upload a PDF file"}
@app.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)):
    # Check if the uploaded file is a PDF file
    if file.filename.endswith(".pdf"):
        # Open the uploaded PDF file using PyMuPDF
        doc = fitz.open(stream=file.file.read(), filetype="pdf")
        ARTICLE = ""
        for page in doc:
            text = page.get_text()
            ARTICLE += text

        # Using the summariser to generate a summary and return it
        summary = summarizer(ARTICLE, max_length=100, min_length=30, do_sample=False)

        # Render the HTML template with the summary content
        template = env.get_template('summary.html')
        html = template.render(summary=summary[0]["summary_text"])

        return HTMLResponse(content=html, status_code=200)
    else:
        return {"error": "Only PDF files are supported"}


@app.get("/static/summary.css")
async def get_css():
    return FileResponse("summary.css", media_type="text/css")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)