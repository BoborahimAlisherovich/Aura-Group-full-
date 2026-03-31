# AURA Group - Corporate Website

<p align="center">
  <img src="static/imgs/logo_image/logo_transparent.png" alt="AURA Group" width="150" height="150">
</p>
<h3 align="center">Loyiha tezligi, tartibi va sifati bitta joyda!</h3>

## 📋 Loyiha haqida

**AURA Group** - zamonaviy IT kompaniyai uchun yaratilgan korporativ veb-sayt. Ushbu loyiha yordamida tashkilotning barcha xizmatlari, portfoliosi, jamoa a'zolari va bo'sh ish o'rinlari namoyish qilinadi. Sayt mukammal **UI/UX** dizayni asosida, eng tezkor ishlash rejimlariga moslab qurilgan hamda premium **3D (Glassmorphism, Lottie Animation)** effektlarni o'z ichiga oladi.

### ✨ Asosiy xususiyatlar

- 🌍 **Ko'p tilli arxitektura** - O'zbek, Rus va Ingliz tillarini to'liq qo'llab-quvvatlaydi (`django.po` orqali AI qilingan tarjimalar jamlanmasi)
- 📱 **O'ta sezgir (Ultra Responsive)** - Barcha qurilmalarda (mobil, planshet, kompyuter) mukammal ishlaydigan format (UI/UX)
- 🎭 **Premium UI/UX va "Wow" effekt** - Glassmorphism, Harakatlanuvchi 3D robot animasiyasi, Maxsus Preloader
- ⚡ **Yuqori tezlik** - Rasmlarning maxsus (`Lazy Load`) turida yuklanishi oqibatida serverga yukni keskin tushirish
- 🤖 **Telegram bot integratsiyasi** - Mijozlar aloqa formasidan tushgan barcha so'rovlar menejer telegramiga bir zumda jo'natiladi
- 🔥 **Custom Neon Cursor** - Mijozlarning diqqatini bo'lmaydigan va zavq beruvchi zamonaviy xarakatlanuvchi nuqta (sichqoncha)

---

## 🛠️ Texnologiyalar

| Texnologiya | Versiya | Tavsif |
|-------------|---------|--------|
| Python | 3.12+ | Bosh backend tili |
| Django | 5.2.11 | Asosiy Web framework |
| django-modeltranslation | 0.19.19 | Ma'lumotlar bazasini ko'p dilda olib borish |
| HTML5 / CSS3 / JS | - | Front-end UI qismi |
| LottieFiles | - | 3D Robot animatsiyasi qismi |
| Swiper.js / Particles.js | - | Slayder va orqafon uchun zamonaviy harakatdagi zarralar |
| deep-translator | - | Terminal orqali matnlarni avtomatik o'giruvchi AI vositachisi |

---

## 📁 Loyiha tuzilishi

```text
AURA Group/
├── 📂 auragroup/          # Asosiy Django ilovasi (App)
│   ├── admin.py           # Premium admin panel
│   ├── models.py          # Database strukturalari (Xizmatlar, Jamoa, Portfolio, va hokazo)
│   ├── views.py           # Frontend uchun kontrollerlar
│   ├── urls.py            # Ichki yo'nalishlar
│   ├── bot.py             # Telegram bot avtomatizatsiyasi
│   └── translation.py     # Modellar rus-en tillari tarjimasi ustunlari
├── 📂 config/             # Django loyihasining root (boshqaruv) strukturasi
├── 📂 templates/          # HTML shablonlari va UI frontend fayllar
├── 📂 static/             # Frontend Assets (CSS, JS, Rasmlar)
├── 📂 locale/             # Sayt bazasiga tegishli matnlarni ("po" va "mo" formatlar) tillari bo'limi
├── 📂 media/              # Yuklangan surat va bazadagi fayllar maskani
├── manage.py              # Asosiy ijrochi fayl
└── README.md              # Siz o'qiyotgan ushbu hujjat
```

---

## 🚀 O'rnatish qo'llanmasi qadam va qadam

### 1. Repozitoriyani klonlash

```bash
git clone https://github.com/BoborahimAlisherovich/Aura-Group-full-.git
cd Aura-Group-full-
```

### 2. Virtual muhit yaratish va uni faollashtirish

```bash
# Windows foydalanuvchilari ushun
python -m venv venv
.\venv\Scripts\activate

# Linux yoki Mac foydalanuvchilari uchun
python3 -m venv venv
source venv/bin/activate
```

### 3. Talab qilingan dasturlarni (packages) o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Muhit o'zgaruvchilarini (`.env`) sozlash
Katalogning asosiy qismida (manage.py bor muhitda) `.env` faylini yarating va quyidagi satrlarni o'zgaritib yozing:

```env
SECRET_KEY=sizing_maxfiy_django_kodingiz
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Telegram bot integratsiyasi (so'rovnomalar botga kelishi uchun)
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
TELEGRAM_CHAT_ID=YOUR_CHAT_ID_HERE
```

### 5. Ma'lumotlar bazasini qabul qilish

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Admin profilini yaratish

```bash
python manage.py createsuperuser
```

### 7. Loyihadagi barcha tarjimalarni tizimga (mo formatda) kiritish

```bash
python manage.py compilemessages -l en -l ru
```

### 8. Loyihani jonli tarzda ishga tushirish

```bash
python manage.py runserver
```

🌐 **Sayt manzili:** http://127.0.0.1:8000  
🔒 **Admin panel idorasi:** http://127.0.0.1:8000/admin

---

## 📝 Xavfsizlik yo'riqnomasi (Production/Deploy uchun)

Saytni to'g'ridan-to'g'ri serverga (hosting - masalan VPS/VDS) o'tkazilayotgan holatda qo'yidagi harakatlarni bajarish shart:
- `settings.py` (yoki `.env` faylda) ichidagi `DEBUG = False` holatiga tushurilishi kerak aks holda sizning loyihadagi muammoli ma'lumotlar hammaga ko'rinib qoladi.
- `ALLOWED_HOSTS` ro'yxatiga ishlab chiqilayotgan (olib bo'lingan) asl domeningiz va IP addres yozilishi lozim. Misol: `['auragroup.uz', 'www.auragroup.uz']`
- Eng oxirida server barcha css kodlarni tanishi uchun `python manage.py collectstatic` orqali statik fayllarni "jami" qilib biriktirib olinishi zarur.

---

## 📞 Aloqa
Saytga tegishli savollar bo'lsa yoki yaxshilashda fikr takliflar bo'yicha ma'lumot qoldirish:

- 🌐 **Sayt:** [auragroup.uz](https://auragroup.uz)
- 📧 **Elektron pochta (Email):** info@auragroup.uz
- 📱 **Telegram tarmoq:** [@AuraGroupAdmin](https://t.me/AuraGroupAdmin)
- 📍 **Obyekt Manzil:** Toshkent sh., Sergeli tumani, PDP University

---

<p align="center">
  <b>AURA Group</b> © 2024-2026. Barcha huquqlar himoyalangan va ishonchli nazorat ostida!
</p>
