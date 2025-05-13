import os
from dotenv import load_dotenv
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from nlp import extract_doc_text, extract_pdf_text, summarize_text, extract_tags
from crud import add_to_vault, delete_from_vault, get_from_vault
from sqlalchemy.orm import Session
from database import SessionLocal
from models import VaultItem, CreateVaultItem
from typing import List

# Load .env values
load_dotenv()
UPLOAD_DIR = os.getenv('UPLOAD_DIR')

# Initialize router
router = APIRouter(prefix='/vault', tags=['vault'])

# Function to get session instance
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint for uploading a file
@router.post('/upload', response_model = VaultItem)
async def upload_file(file: UploadFile=File(...), db : Session = Depends(get_db)):
    if not file.filename.endswith(('.docx', '.pdf')):
        raise HTTPException(status_code=400, detail='Only PDF or Docs can be added')
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, 'wb') as f:
        f.write(await file.read())

    content : str
    if file.filename.endswith('.pdf'):
        content = extract_pdf_text(file_path)
    else:
        content = extract_doc_text(file_path)

    summaryText = summarize_text(content) # Summarize
    summaryTags = extract_tags(content)

    # Add to database
    tempVaultItem = CreateVaultItem(summary=summaryText, filename=file.filename, tags=','.join(summaryTags))

    vaultItem = add_to_vault(db, tempVaultItem)

    return vaultItem
    
@router.get('/get_item', response_model = List[VaultItem])
def get_vault_item(db : Session=Depends(get_db)):
    return get_from_vault(db)

@router.delete('/{item_id}', response_model=VaultItem)
def delete_vault_item(item_id : int, db: Session=Depends(get_db)):
    db_item = delete_from_vault(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=400, detail='Element not present in list..')
    else:
        return db_item
