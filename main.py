from fastapi import FastAPI
from pydantic import BaseModel
from file_analiser import signature
import os

app = FastAPI()

class FileCheckRequest(BaseModel):
    file_path: str

class SendingSignature:
    def __init__(self, processed_data=signature):
        self.file_name = processed_data.file_name
        self.expected_signatures = []
        for sig in processed_data.expected_signatures:
            self.expected_signatures.append(sig.hex())
        self.actual_signature = processed_data.actual_signature.hex()
        self.match_signature = processed_data.match_signature

@app.get("/check-signature")
def get_magic_number_confirmation(request: FileCheckRequest):
    file_signature = signature(request.file_path)
    
    # Convert the raw bytes to a hexadecimal string using .hex()
    return {
        "path": request.file_path, 
        "signature": SendingSignature(file_signature)
    }
    file_signature = signature(file_path)

    if not os.path.exists(file_path):
        return {"error": f"File not found at: {file_path}"}

    response = {
        "file": file_signature.file_name,
        "expected_signatures": file_signature.expected_signatures,
        "actual_signature": file_signature.actual_signature,
        "match": file_signature.match_signature
    }
    del file_signature
    return response