import requests
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = "7935151260:AAFEylpFNSQFbmrYqeF_vKwtsUDMotZpA9c"
CHAT_ID = 1718572899


def send_message(name, email, phone_number, description):
    """Aloqa xabarini Telegram botga yuborish"""
    text = (
        f"📥 <b>Yangi xabar!</b>\n\n"
        f"👤 <b>Ism:</b> {name}\n"
        f"📧 <b>Email:</b> {email}\n"
        f"📱 <b>Tel:</b> {phone_number}\n\n"
        f"📝 <b>Xabar:</b>\n{description}"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML',
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("✅ Xabar Telegramga yuborildi")
    except Exception as e:
        print("❌ Xabar yuborishda xatolik:", e)


def send_service_request(company, phone, service, contact_name, description, telegram="", email="", file_path=None):
    """Xizmat buyurtmasini Telegram botga yuborish"""
    print("Bot token:", BOT_TOKEN)
    print("Chat ID:", CHAT_ID)
    API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    text = (
        f"🆕 <b>Yangi xizmat buyurtmasi!</b>\n\n"
        f"🏢 <b>Kompaniya:</b> {company}\n"
        f"👤 <b>Ism familiya:</b> {contact_name}\n"
        f"📞 <b>Telefon:</b> {phone}\n"
        f"📱 <b>Telegram:</b> {telegram}\n"
        f"📧 <b>Email:</b> {email}\n"
        f"🛠 <b>Xizmat turi:</b> {service}\n\n"
        f"📝 <b>Loyiha tavsifi:</b>\n{description}"
    )
    data = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML',
    }
    try:
        resp = requests.post(API_URL, data=data)
        resp.raise_for_status()
        print("✅ Telegramga yuborildi")
    except requests.RequestException as e:
        print(f"❌ Xatolik: {e}")
    
    # Fayl yuborish (agar mavjud bo'lsa)
    if file_path:
        send_file_to_telegram(file_path, f"{contact_name} - {service} buyurtmasi")


def send_file_to_telegram(file_path, caption="Fayl"):
    """Faylni Telegram botga yuborish"""
    API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'
    
    try:
        with open(file_path, 'rb') as file:
            files = {'document': file}
            data = {
                'chat_id': CHAT_ID,
                'caption': f"📎 {caption}",
            }
            resp = requests.post(API_URL, data=data, files=files)
            resp.raise_for_status()
            print("✅ Fayl Telegramga yuborildi")
    except FileNotFoundError:
        print(f"❌ Fayl topilmadi: {file_path}")
    except requests.RequestException as e:
        print(f"❌ Fayl yuborishda xatolik: {e}")


def send_vocation(mgs_data: dict, resume_path=None):
    """Vakansiya arizasini Telegram botga yuborish"""
    print("Bot token:", BOT_TOKEN)
    print("Chat ID:", CHAT_ID)
    
    # Avval matn xabarini yuborish
    API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    text = "📋 <b>Yangi vakansiya arizasi!</b>\n\n"
    for k, v in mgs_data.items():
        text += f"<b>{k}:</b> {v}\n"

    data = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML',
    }
    try:
        resp = requests.post(API_URL, data=data)
        resp.raise_for_status()
        print("✅ Matn Telegramga yuborildi")
    except requests.RequestException as e:
        print(f"❌ Matn yuborishda xatolik: {e}")
    
    # Resume faylini yuborish (agar mavjud bo'lsa)
    if resume_path:
        send_resume_file(resume_path, mgs_data.get('Ism', 'Nomzod'))


def send_resume_file(file_path, applicant_name="Nomzod"):
    """Resume faylini Telegram botga yuborish"""
    API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'
    
    try:
        with open(file_path, 'rb') as file:
            files = {'document': file}
            data = {
                'chat_id': CHAT_ID,
                'caption': f"📄 {applicant_name} ning resume fayli",
            }
            resp = requests.post(API_URL, data=data, files=files)
            resp.raise_for_status()
            print("✅ Resume fayli Telegramga yuborildi")
    except FileNotFoundError:
        print(f"❌ Fayl topilmadi: {file_path}")
    except requests.RequestException as e:
        print(f"❌ Resume yuborishda xatolik: {e}")


