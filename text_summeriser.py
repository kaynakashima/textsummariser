from fastapi import FastAPI, File, UploadFile
from fastapi.responses import RedirectResponse, HTMLResponse
from transformers import pipeline
from huggingface_hub import login
from jinja2 import Template
import fitz

app =FastAPI()

template = """
<!DOCTYPE html>
<html>
  <body>
    <h1>PDF Summarizer</h1>
    <form action="http://localhost:8000/summarize" method="post" enctype="multipart/form-data" target="_blank">
      <input type="file" name="file" accept="application/pdf">
      <input type="submit" value="Summarize">
    </form>
  </body>
</html>
"""

jinja_template = Template(template)

# Load a summarization model using Hugging Face's Inference API
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Authenticate with hugging face token
token = "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"
login(token=token)

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
        # Save the uploaded PDF file to disk
        with open(file.filename, "wb") as f:
            f.write(file.file.read())

        # Open the uploaded PDF file using PyMuPDF
        doc = fitz.open(file.filename)
        ARTICLE = ""
        for page in doc:
            text = page.get_text()
            ARTICLE += text

        # Using the summariser to generate a summary and return it
        summary = summarizer(ARTICLE, max_length=100, min_length=30, do_sample=False)

        #create HTML response
        html = f"""
           <html>
             <body>
               <h1>Summary</h1>
               <p>{summary}</p>
             </body>
           </html>
           """
        return HTMLResponse(content=html, status_code=200)
    else:
        return {"error": "Only PDF files are supported"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)