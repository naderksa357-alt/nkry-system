from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os

# تعريف التطبيق أولاً
app = FastAPI()

# الصفحة الرئيسية
@app.get("/")
def home():
    return {"message": "NKRY system is running"}

# صفحة اختبار
@app.get("/order", response_class=HTMLResponse)
def order_page():
    return "<h2>Order page works</h2>"

# Webhook (سنحتاجه لاحقاً للواتساب)
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Incoming:", data)
    return {"status": "received"}

# تشغيل السيرفر
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
