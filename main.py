from fastapi import FastAPI, Header
from file_analiser import signature

app = FastAPI()

class SendingSignature:
    def __init__(self, processed_data=signature):
        self.file_name = processed_data.file_name
        self.expected_signatures = []
        for sig in processed_data.expected_signatures:
            self.expected_signatures.append(sig.hex())
        self.actual_signature = processed_data.actual_signature.hex()
        self.match_signature = processed_data.match_signature

@app.get("/check-signature")
def get_magic_number_confirmation(file_path: str = Header(...)):
    file_signature = signature(file_path)
    
    # Convert the raw bytes to a hexadecimal string using .hex()
    return {
        "path": file_path, 
        "signature": SendingSignature(file_signature)
    }