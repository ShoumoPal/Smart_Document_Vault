from transformers import pipeline
from keybert import KeyBERT
from pdfminer.high_level import extract_text
from docx import Document

# Load Huggingface model
summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
kw_model = KeyBERT()

# Extract text
def extract_pdf_text(path:str) -> str:
    return extract_text(path)

def extract_doc_text(path:str) -> str:
    doc = Document(path)
    temp = []
    for p in doc.paragraphs:
        temp.append(p.text)
    
    return '\n'.join(temp)

# Summarize text

def summarize_text(text:str) -> str:
    if len(text) > 1024:
        text = text[:1024]

    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Extract tags

def extract_tags(text: str, top_n: int = 5) -> list:
    keywords = kw_model.extract_keywords(text, stop_words='english', top_n=top_n)
    return [kw for kw, _ in keywords]

