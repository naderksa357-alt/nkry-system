from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

# تعريف التطبيق أولاً (مهم)
app = FastAPI()


@app.get("/")
def home():
    return {"message": "NKRY system is running"}


@app.get("/order", response_class=HTMLResponse)
def order():
    return """
    <h2>طلب منتج NKRY</h2>
    <form action="https://wa.me/966502888357">
        الاسم:<br>
        <input type="text" name="text"><br><br>

        الجوال:<br>
        <input type="text" name="text"><br><br>

        المدينة:<br>
        <input type="text" name="text"><br><br>

        المنتج:<br>
        <input type="text" name="text"><br><br>

        <button type="submit">إرسال الطلب عبر واتساب</button>
    </form>
    """


# تشغيل على Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
