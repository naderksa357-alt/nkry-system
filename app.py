from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os

# لازم تعريف app أولاً
app = FastAPI()

@app.get("/")
def home():
    return {"message": "NKRY system is running"}

@app.get("/order", response_class=HTMLResponse)
def order_page():
    return "<h1>Order page works</h1>"

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Incoming:", data)
    return {"status": "received"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
