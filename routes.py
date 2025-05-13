import os
from dotenv import load_dotenv
from fastapi import APIRouter, File, UploadFile, HTTPException

# Load .env values
load_dotenv()
UPLOAD_DIR = os.getenv('UPLOAD_DIR')

router = APIRouter()

# Endpoint for uploading a file
@router.post('/upload')
async def upload_file(file: UploadFile=File(...)):
    if not file.filename.endswith(('.docx', '.pdf')):
        raise HTTPException(status_code=400, detail='Only PDF or Docs can be added')
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, 'wb') as f:
        f.write(await file.read())

    return {'filename':file.filename, 'message':'File uploaded successfully'}

