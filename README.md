# 📄 Smart Document Vault API

An AI-powered FastAPI backend that allows users to upload `.pdf` or `.docx` files, automatically extract text, generate summaries, and tag documents using local NLP models — all without relying on cloud services or paid APIs.

---

## 🚀 Features

- 🔐 Upload `.pdf` and `.docx` files securely
- 🧠 AI-powered **text summarization** using BART (HuggingFace)
- 🏷️ Smart **keyword tagging** via KeyBERT
- 🗃️ Stores document metadata (summary, filename, tags) in **PostgreSQL**
- 🔎 Endpoints to **list**, **delete**, and (optionally) **search** documents
- ✅ Fully local and free — no cloud subscriptions required

---

## 🧰 Tech Stack

| Layer           | Technology                      |
|----------------|----------------------------------|
| Web Framework   | FastAPI                         |
| Language        | Python 3.10+                    |
| AI/NLP          | HuggingFace Transformers (`bart-large-cnn`), KeyBERT |
| File Parsing    | `pdfminer.six`, `python-docx`   |
| Database        | PostgreSQL + SQLAlchemy         |
| Deployment-Ready| Uvicorn                         |

---

## 🧪 Endpoints

| Method | Endpoint           | Description                   |
|--------|--------------------|-------------------------------|
| POST   | `/vault/upload`     | Upload and analyze a document |
| GET    | `/vault/get_item`   | Get all stored documents      |
| DELETE | `/vault/{item_id}`  | Delete document by ID         |

---

## 🗂 Example Upload Response

```json
{
  "id": 7,
  "summary": "This document discusses...",
  "tags": ["python", "backend", "architecture"]
}
