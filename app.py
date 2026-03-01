@app.route('/moyasar-webhook', methods=['POST'])
def moyasar_webhook():
    data = request.json
    # التأكد من نجاح الدفع
    if data['status'] == 'paid':
        order_id = data['metadata']['order_id'] # رقم الطلب المخزن
        
        # 1. تحديث حالة الطلب في Supabase إلى (تم الدفع - جارِ التنفيذ)
        supabase.table("orders_agents").update({"status": "Paid"}).eq("id", order_id).execute()
        
        # 2. إرسال رسالة واتساب تلقائية للعميل عبر Twilio
        send_whatsapp_msg(data['metadata']['phone'], "تم استلام مبلغك بنجاح! فريق NKRY بدأ الآن في تجهيز طلبك.")
        
        # 3. إرسال إيميل رسمي للعميل يحتوي على الفاتورة وتفاصيل الخشب والمقاسات
        send_official_email(data['metadata']['email'], "تأكيد طلب أثاث - NKRY")
        
    return "OK", 200
    
