from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

# إنشاء التطبيق أولاً
app = FastAPI()

# الصفحة الرئيسية
@app.get("/")
def home():
    return {"message": "NKRY system is running"}

# صفحة الطلب
@app.get("/order", response_class=HTMLResponse)
def order():
    return """
    <h1>NKRY Order Page</h1>
    <p>The system is working successfully</p>
    """

# تشغيل السيرفر
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
