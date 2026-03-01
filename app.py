from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NKRY system is running"}

@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.json()
    print("Incoming message:", data)
    return {"status": "received"}
