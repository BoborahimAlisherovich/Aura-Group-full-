# AURA Group - Corporate Website

<p align="center">
  <img src="static/imgs/header-img.avif" alt="AURA Group" width="100%">
</p>

## 📋 Loyiha haqida

**AURA Group** - zamonaviy korporativ veb-sayt. Django framework asosida qurilgan, ko'p tilli qo'llab-quvvatlash (O'zbek, Rus, Ingliz) va professional UI/UX dizayn bilan.

### ✨ Asosiy xususiyatlar

- 🌐 **Ko'p tilli** - O'zbek, Rus, Ingliz tillarida to'liq tarjima
- 📱 **Responsive dizayn** - Barcha qurilmalarda mukammal ko'rinish
- 🎨 **Zamonaviy UI** - UIC.group uslubidagi professional navbar
- 📧 **Aloqa formasi** - Telegram bot integratsiyasi
- 💼 **Portfolio** - Loyihalar galereyasi
- 👥 **Jamoa** - Xodimlar haqida ma'lumot
- 📰 **Blog/Yangiliklar** - Kontentni boshqarish
- 💼 **Karyera** - Vakansiyalar va ariza qabul qilish

---

## 🛠️ Texnologiyalar

| Texnologiya | Versiya | Tavsif |
|-------------|---------|--------|
| Python | 3.12+ | Asosiy dasturlash tili |
| Django | 6.0.1 | Web framework |
| django-modeltranslation | 0.19+ | Ko'p tilli modellar |
| Pillow | 11.0+ | Rasmlar bilan ishlash |
| python-telegram-bot | 21.0+ | Telegram bot integratsiyasi |
| Swiper.js | 11.0+ | Slider/Carousel |

---

## 📁 Loyiha tuzilishi

```
AURA Group/
├── 📂 auragroup/          # Asosiy Django ilovasi
│   ├── admin.py           # Admin panel sozlamalari
│   ├── models.py          # Ma'lumotlar modellari
│   ├── views.py           # Ko'rinishlar (views)
│   ├── urls.py            # URL marshrutlari
│   ├── forms.py           # Formalar
│   └── bot.py             # Telegram bot
│
├── 📂 config/             # Django konfiguratsiyasi
│   ├── settings.py        # Asosiy sozlamalar
│   ├── urls.py            # Asosiy URL marshrutlari
│   └── wsgi.py            # WSGI konfiguratsiyasi
│
├── 📂 templates/          # HTML shablonlar
│   ├── base.html          # Asosiy shablon
│   ├── index.html         # Bosh sahifa
│   ├── about.html         # Biz haqimizda
│   ├── services.html      # Xizmatlar
│   ├── portfolio.html     # Portfolio
│   ├── career.html        # Karyera
│   └── contact.html       # Aloqa
│
├── 📂 static/             # Statik fayllar
│   ├── css/               # CSS stillari
│   ├── js/                # JavaScript
│   └── imgs/              # Rasmlar
│
├── 📂 locale/             # Tarjimalar
│   ├── en/LC_MESSAGES/    # Ingliz tili
│   ├── ru/LC_MESSAGES/    # Rus tili
│   └── uz/LC_MESSAGES/    # O'zbek tili
│
├── 📂 media/              # Yuklangan fayllar
│   ├── Images/            # Rasmlar
│   └── files/             # Hujjatlar
│
├── manage.py              # Django CLI
├── Pipfile                # Paketlar ro'yxati
└── README.md              # Ushbu fayl
```

---

## 🚀 O'rnatish

### 1. Repozitoriyani klonlash

```bash
git clone https://github.com/auragroup/website.git
cd website
```

### 2. Virtual muhit yaratish

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Paketlarni o'rnatish

```bash
pip install -r requirements.txt
# yoki Pipenv bilan
pipenv install
```

### 4. Muhit o'zgaruvchilarini sozlash

`.env` fayl yarating:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Telegram Bot
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_CHAT_ID=your-chat-id

# Database (ixtiyoriy - default SQLite)
DATABASE_URL=postgres://user:pass@localhost/dbname
```

### 5. Ma'lumotlar bazasini migratsiya qilish

```bash
python manage.py migrate
```

### 6. Admin foydalanuvchi yaratish

```bash
python manage.py createsuperuser
```

### 7. Tarjimalarni kompilyatsiya qilish

```bash
python manage.py compilemessages
# yoki
python compile_messages.py
```

### 8. Serverni ishga tushirish

```bash
python manage.py runserver
```

🌐 Sayt: http://127.0.0.1:8000  
🔐 Admin: http://127.0.0.1:8000/admin

---

## 🌍 Ko'p tilli qo'llab-quvvatlash

### Qo'llab-quvvatlanadigan tillar

| Til | Kod | URL |
|-----|-----|-----|
| 🇺🇿 O'zbek | `uz` | `/uz/` (default) |
| 🇷🇺 Rus | `ru` | `/ru/` |
| 🇬🇧 Ingliz | `en` | `/en/` |

### Tarjima qo'shish

1. **Matnlarni belgilash:**
```python
from django.utils.translation import gettext_lazy as _

title = _("Biz haqimizda")
```

2. **Tarjimalarni chiqarish:**
```bash
python manage.py makemessages -l ru -l en
```

3. **`.po` fayllarni tahrirlash:**
```
locale/ru/LC_MESSAGES/django.po
locale/en/LC_MESSAGES/django.po
```

4. **Kompilyatsiya qilish:**
```bash
python manage.py compilemessages
```

---

## 📧 Telegram Bot integratsiyasi

Aloqa formasi orqali kelgan xabarlar Telegram botga yuboriladi.

### Sozlash

1. [@BotFather](https://t.me/BotFather) orqali bot yarating
2. Token va Chat ID ni `.env` faylga qo'shing:

```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=-1001234567890
```

---

## 🎨 Dizayn tizimi

### Ranglar

| Rang | Hex | Ishlatilishi |
|------|-----|--------------|
| Primary | `#0066FF` | Tugmalar, linklar |
| Secondary | `#1a1a2e` | Sarlavhalar |
| Accent | `#00C9A7` | Gradient |
| Background | `#f8fafc` | Fon |
| Text | `#64748b` | Matn |

### Navbar

Navbar UIC.group uslubida yaratilgan:
- Scroll paytida shaffofdan oq rangga o'tish
- Rounded tugmalar va linklar
- Kompakt til almashtiruvchi

---

## 📱 Admin Panel

Admin panel quyidagi xususiyatlarga ega:

- 📊 **Dashboard** - Statistika
- 🖼️ **Rasm preview** - Rasmlarni ko'rish
- 🏷️ **Status badge** - Rang kodlari
- 📎 **Fayl yuklash** - Resume, rasmlar
- 🔍 **Qidiruv va filtr** - Tez topish

### Kirish

```
URL: /admin/
Login: admin
Password: ********
```

---

## 🧪 Testlar

```bash
python manage.py test
```

---

## 📦 Deploy

### Production sozlamalari

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['auragroup.uz', 'www.auragroup.uz']
SECURE_SSL_REDIRECT = True
```

### Statik fayllar

```bash
python manage.py collectstatic
```

---

## 🤝 Hissa qo'shish

1. Fork qiling
2. Branch yarating (`git checkout -b feature/yangi-xususiyat`)
3. O'zgarishlarni commit qiling (`git commit -m 'Yangi xususiyat qo'shildi'`)
4. Push qiling (`git push origin feature/yangi-xususiyat`)
5. Pull Request yarating

---

## 📄 Litsenziya

MIT License - batafsil [LICENSE](LICENSE) faylida.

---

## 📞 Aloqa

- 🌐 Sayt: [auragroup.uz](https://auragroup.uz)
- 📧 Email: info@auragroup.uz
- 📱 Telegram: [@auragroup](https://t.me/auragroup)
- 📍 Manzil: Toshkent, O'zbekiston

---

<p align="center">
  <b>AURA Group</b> © 2024-2026. Barcha huquqlar himoyalangan.
</p>
