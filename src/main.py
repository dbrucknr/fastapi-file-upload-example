# Native Python Libraries
from os import path
from typing import Annotated

# Third Party Libraries
from aiofiles import open
from pydantic import BaseModel
from fastapi.responses import ORJSONResponse
from fastapi import FastAPI, File, UploadFile

# API Instance
api = FastAPI(
    title="File Upload API",
    description="API to upload files",
    version="0.1.0",
    default_response_class=ORJSONResponse,
)

# Constants
UPLOAD_DIR = "uploads"


# Schemas
class FileUploadResponse(BaseModel):
    filename: str
    file_mime_type: str


@api.post("/upload-file", response_model=FileUploadResponse)
async def upload_file(file: Annotated[UploadFile, File(...)]):
    # Step 1: Construct the file path
    file_path = path.join(UPLOAD_DIR, file.filename)
    # Step 2: Save the file using non-blocking IO
    async with open(file_path, "wb") as saved_file:
        # Step 3: Asynchronously read chunks of 1024 bytes
        while content := await file.read(1024):
            # Step 4: Write the chunked content to the file_path
            await saved_file.write(content)

    return {
        "filename": file.filename,
        "file_mime_type": file.content_type,
    }
