from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

# تعريف التطبيق أولاً
app = FastAPI()

@app.get("/")
def home():
    return {"message": "NKRY system is running"}

# تشغيل السيرفر (مهم لـ Railway)
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
