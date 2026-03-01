from fastapi.responses import RedirectResponse

@app.post("/submit-order")
def submit_order(
    name: str = Form(...),
    phone: str = Form(...),
    city: str = Form(...),
    product: str = Form(...)
):
    message = f"""
New Order:
Name: {name}
Phone: {phone}
City: {city}
Product: {product}
"""

    whatsapp_number = "9665XXXXXXXX"  # ضع رقمك هنا بدون +
    url = f"https://wa.me/{whatsapp_number}?text={message}"

    return RedirectResponse(url=url)
