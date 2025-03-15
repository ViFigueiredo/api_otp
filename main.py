from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyotp

app = FastAPI()

class OTPRequest(BaseModel):
    secret: str

@app.post("/generate_otp")
def generate_otp(request: OTPRequest):
    # Cria um objeto TOTP com a chave secreta fornecida
    totp = pyotp.TOTP(request.secret)
    # Gera um código OTP
    otp_code = totp.now()
    return {"otp": otp_code}

@app.post("/verify_otp")
def verify_otp(request: OTPRequest, otp: str):
    # Cria um objeto TOTP com a chave secreta fornecida
    totp = pyotp.TOTP(request.secret)
    # Verifica se o código OTP fornecido é válido
    is_valid = totp.verify(otp)
    return {"valid": is_valid}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)