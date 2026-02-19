from pathlib import Path


MAPPING = {
    "Bizning jamoamizga qo'shilmoqchimisiz?": "Хотите присоединиться к нашей команде?",
    "Nega AURA Group da ishlash kerak?": "Почему стоит работать в AURA Group?",
    "Qanday qo'shilish mumkin?": "Как можно присоединиться?",
    "Savollaringiz bormi?": "Есть вопросы?",
    "AURA Group | Raqamli Mahsulotlar Injiringi": "AURA Group | Инжиниринг цифровых продуктов",
    "Biznes o'sishini tezlashtiradigan IT hamkor": "IT-партнер, ускоряющий рост бизнеса",
    "AURA Group bilan kuchli raqamli mahsulot yarating va bozorga tez chiqing": "Создавайте сильные цифровые продукты с AURA Group и выходите на рынок быстрее",
    "Biz strategiya, UX/UI va engineering'ni bitta tizimga birlashtirib, kompaniyangizga real natija beradigan platformalar ishlab chiqamiz: tezroq ishga tushish, yuqori konversiya va barqaror o'sish.": "Мы объединяем стратегию, UX/UI и инженерную разработку в единую систему и создаем платформы с реальными бизнес-результатами: быстрый запуск, высокая конверсия и устойчивый рост.",
    "Loyihani boshlash": "Начать проект",
    "Case study ko'rish": "Смотреть кейсы",
    "Muddatga rioya ko'rsatkichi": "Показатель соблюдения сроков",
    "Mahsulot chiqarish tezligi o'sishi": "Рост скорости выпуска продукта",
    "Biz qanday qiymat beramiz": "Какую ценность мы даем",
    "Biznes tahlili va aniq texnik yechim xaritasi": "Бизнес-анализ и четкая карта технических решений",
    "Konversiyaga yo'naltirilgan premium UX/UI": "Премиальный UX/UI, ориентированный на конверсию",
    "Masshtablanuvchi backend va cloud arxitektura": "Масштабируемый backend и облачная архитектура",
    "KPI bilan o'lchanadigan release jarayoni": "Процесс релиза с измерением по KPI",
    "Tezroq bozorga chiqish": "Быстрый выход на рынок",
    "Mijoz ishonchi va o'sish": "Доверие клиентов и рост",
    "Biz kod yozmaymiz, biznes natija beradigan tizim quramiz": "Мы не просто пишем код — мы строим системы, которые дают бизнес-результат",
    "AURA Group product fikrlash asosida ishlaydi: maqsadni aniqlaymiz, foydalanuvchi oqimini tozalaymiz va texnik arxitekturani kelajakdagi o'sish uchun tayyorlaymiz.": "AURA Group работает на основе product-подхода: определяем цель, улучшаем пользовательские сценарии и готовим архитектуру к будущему росту.",
    "Turli sohalarda real tajriba: fintech, logistika, ta'lim, healthcare.": "Реальный опыт в разных сферах: fintech, логистика, образование, healthcare.",
    "Yuqori yuklama tizimlari uchun doimiy monitoring va qo'llab-quvvatlash.": "Постоянный мониторинг и поддержка для высоконагруженных систем.",
    "Har bir bosqichda tajribali mutaxassislar bilan ishlaysiz.": "На каждом этапе вы работаете с опытными специалистами.",
    "Biznes vazifangizga mos full-cycle IT xizmatlar": "Full-cycle IT-услуги под ваши бизнес-задачи",
    "Har bir loyiha KPI, muddat va sifat bo'yicha nazorat qilinadigan delivery modeli asosida olib boriladi.": "Каждый проект ведется по delivery-модели с контролем KPI, сроков и качества.",
    "Xizmatni tanlash": "Выбрать услугу",
    "MVP'dan enterprise platformagacha bo'lgan to'liq engineering jarayoni.": "Полный engineering-процесс от MVP до enterprise-платформы.",
    "Real biznes natija bergan case study loyihalar": "Кейсы с реальным бизнес-эффектом",
    "Bitta oynada 4 ta loyiha ko'rinadi, strelkalar orqali keyingi loyihalarga silliq o'tasiz.": "В одном окне видно 4 проекта, переход к следующим выполняется плавно стрелками.",
    "Oldingi loyihalar": "Предыдущие проекты",
    "Keyingi loyihalar": "Следующие проекты",
    "Loyihalar qo'shilmoqda": "Проекты добавляются",
    "Yaqin kunlarda yangi loyihalarimizni bu yerda e'lon qilamiz.": "В ближайшие дни мы опубликуем здесь новые проекты.",
    "Portfolio sahifasi": "Страница портфолио",
    "Ishonchli stack, zamonaviy arxitektura, tez delivery": "Надежный стек, современная архитектура, быстрая delivery",
    "Sohalar": "Отрасли",
    "Murakkab biznes modellarga mos yechimlar": "Решения для сложных бизнес-моделей",
    "To'lovlar, onboarding va xavfsiz tranzaksiya oqimlari.": "Платежи, онбординг и безопасные транзакционные потоки.",
    "Real-time kuzatuv va operatsion boshqaruv paneli.": "Панели мониторинга и операционного управления в реальном времени.",
    "Ma'lumotga sezgir, barqaror va xavfsiz platformalar.": "Платформы с высокой чувствительностью к данным, стабильностью и безопасностью.",
    "Retention va engagement oshiruvchi mahsulotlar.": "Продукты, повышающие retention и engagement.",
    "Nega biz?": "Почему мы?",
    "Loyihada tezlik, tartib va sifatni bir vaqtda beramiz": "В проекте одновременно обеспечиваем скорость, порядок и качество",
    "Shaffof jarayon": "Прозрачный процесс",
    "Har sprint bo'yicha aniq status, risk va keyingi qadamlar bilan.": "По каждому спринту — понятный статус, риски и следующие шаги.",
    "Biznesga bog'langan KPI": "KPI, связанные с бизнесом",
    "Yechimlarimiz real ko'rsatkichlar bo'yicha baholanadi.": "Наши решения оцениваются по реальным показателям.",
    "Senior mutaxassislar": "Senior-специалисты",
    "Loyiha davomida bir xil professional jamoa bilan ishlaysiz.": "В течение проекта вы работаете с одной профессиональной командой.",
    "Tahlil": "Анализ",
    "Biznes maqsadi, auditoriya va texnik cheklovlar.": "Бизнес-цели, аудитория и технические ограничения.",
    "Dizayn": "Дизайн",
    "UX oqimlar, UI tizimi va prototiplash.": "UX-сценарии, UI-система и прототипирование.",
    "Ishlab chiqish": "Разработка",
    "QA va release nazorati bilan coding jarayoni.": "Процесс разработки с QA и контролем релизов.",
    "Masshtablash": "Масштабирование",
    "Monitoring, optimizatsiya va growth iteratsiyalari.": "Мониторинг, оптимизация и growth-итерации.",
    "Ish jarayoni": "Процесс работы",
    "Strategiyadan launchgacha puxta boshqaruv": "Четкое управление от стратегии до запуска",
    "Stakeholder intervyu, maqsad KPI va roadmap.": "Интервью со стейкхолдерами, целевые KPI и roadmap.",
    "Arxitektura va UX Blueprint": "Архитектура и UX Blueprint",
    "Texnik yechim, dizayn tizimi va sprint rejasi.": "Техническое решение, дизайн-система и план спринтов.",
    "Muntazam demo, QA avtomatizatsiya va CI/CD.": "Регулярные демо, автоматизация QA и CI/CD.",
    "Monitoring, feedback asosida tez iteratsiya.": "Быстрые итерации на основе мониторинга и feedback.",
    "Mijozlar fikri": "Отзывы клиентов",
    "Biz bilan ishlagan rahbarlarning fikrlari": "Отзывы руководителей, которые работали с нами",
    "AURA Group jamoasi KSD82 loyihamizni juda aniq reja asosida olib bordi. Har bir bosqich tushunarli, bajarilish esa ishonchli bo'ldi. Natijada ish jarayonimiz sezilarli darajada tezlashdi.": "Команда AURA Group вела наш проект KSD82 по очень четкому плану. Каждый этап был понятным, исполнение — надежным. В результате наши процессы заметно ускорились.",
    "KSD82 kompaniyasi egasi": "Владелец компании KSD82",
    "Namangan": "Наманган",
    "O'zBA Markaz uchun yaratilgan tizimda dizayn va funksionallik mukammal uyg'unlashdi. Jamoa talabni to'g'ri tushundi va juda sifatli mahsulot topshirdi.": "В системе, созданной для O'zBA Markaz, дизайн и функциональность идеально соединились. Команда правильно поняла требования и сдала очень качественный продукт.",
    "O'zBA Markaz rahbariyati": "Руководство O'zBA Markaz",
    "Toshkent": "Ташкент",
    "eHokimiyat loyihasida AURA Group professionalligi aniq sezildi. Yechimlar barqaror, foydalanuvchi uchun qulay va boshqaruv jarayoniga haqiqiy qulaylik olib keldi.": "В проекте eHokimiyat профессионализм AURA Group был очевиден. Решения оказались стабильными, удобными для пользователей и действительно упростили управленческие процессы.",
    "eHokimiyat loyiha buyurtmachisi": "Заказчик проекта eHokimiyat",
    "Loyihangizni premium darajada ishga tushirishga tayyormisiz?": "Готовы запустить ваш проект на премиальном уровне?",
    "Maqsadingizni yuboring, biz sizga aniq texnik reja va bajarish modelini taqdim etamiz.": "Отправьте вашу цель, и мы предложим точный технический план и модель реализации.",
    "Nega aynan bizni tanlash kerak?": "Почему стоит выбрать именно нас?",
    "Loyihangizni muhokama qilishga tayyormisiz?": "Готовы обсудить ваш проект?",
}


def unq(s: str) -> str:
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return bytes(s, "utf-8").decode("unicode_escape")


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


path = Path("locale/ru/LC_MESSAGES/django.po")
text = path.read_text(encoding="utf-8")
blocks = text.split("\n\n")

updated = 0
out_blocks = []

for block in blocks:
    lines = block.splitlines()
    if not lines or any(l.startswith("#~") for l in lines):
        out_blocks.append(block)
        continue

    msgid = ""
    msgstr = ""
    msgstr_start = None
    msgstr_end = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("msgid "):
            msgid += unq(line[len("msgid "):])
            i += 1
            while i < len(lines) and lines[i].startswith('"'):
                msgid += unq(lines[i])
                i += 1
            continue
        if line.startswith("msgstr "):
            msgstr_start = i
            msgstr += unq(line[len("msgstr "):])
            i += 1
            while i < len(lines) and lines[i].startswith('"'):
                msgstr += unq(lines[i])
                i += 1
            msgstr_end = i - 1
            continue
        i += 1

    if msgid in MAPPING and msgstr_start is not None:
        lines = lines[:msgstr_start] + [f'msgstr "{esc(MAPPING[msgid])}"'] + lines[msgstr_end + 1 :]
        updated += 1

    out_blocks.append("\n".join(lines))

path.write_text("\n\n".join(out_blocks) + "\n", encoding="utf-8")
print(f"updated={updated}")
