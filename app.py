from fastapi import FastAPI, Form, Request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_reply(Body: str = Form(...), From: str = Form(...)):
    # 1. استلام الرسالة من العميل (Body هي نص الرسالة، From هو رقم الجوال)
    customer_msg = Body
    customer_phone = From

    # 2. هنا نرسل الرسالة إلى Claude API (منطق شرحبيل)
    # الوكيل يحلل هل الطلب (طاولة، جهاز بخار، إلخ)
    ai_response = "أبشر، جاري تحليل طلبك للأثاث.." # استبدل هذا بربط Claude API

    # 3. الرد على العميل في الواتساب
    resp = MessagingResponse()
    resp.message(f"مرحباً بك في NKRY \n {ai_response}")
    
    return str(resp)

@app.get("/")
def health_check():
    return {"status": "NKRY System is Online"}
    
