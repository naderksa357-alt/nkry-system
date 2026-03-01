from fastapi import FastAPI, Form
import os

# إنشاء التطبيق
app = FastAPI()

# الصفحة الرئيسية
@app.get("/")
def home():
    return {"message": "NKRY system is running"}

# حفظ طلب
@app.post("/submit-order")
def submit_order(name: str = Form(...), phone: str = Form(...)):
    return {
        "status": "saved",
        "name": name,
        "phone": phone
    }

# تشغيل السيرفر
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
    
