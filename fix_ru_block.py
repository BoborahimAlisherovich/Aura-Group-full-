from pathlib import Path


mapping = {
    "AURA Group - 2025-yil 1-iyulda tashkil etilgan, bizneslar uchun ishonchli va natijador IT hamkor.": "AURA Group — надежный и результативный IT-партнер для бизнеса, основанный 1 июля 2025 года.",
    "Bizning hikoyamiz": "Наша история",
    "Texnologiya va innovatsiya bilan kelajakni bunyod etamiz": "Строим будущее с помощью технологий и инноваций",
    "AURA Group 2025-yil 1-iyulda Boborahim Rustamqulov rahbarligida tashkil etilgan. Kompaniya qisqa muddat ichida bizneslar uchun zamonaviy IT xizmatlarni taqdim etuvchi ishonchli jamoaga aylandi.": "AURA Group была основана 1 июля 2025 года под руководством Боборахима Рустамкулова. За короткое время компания стала надежной командой, предоставляющей современный IT-сервис для бизнеса.",
    "Kompaniyamiz falsafasi O'zbekiston IT bozorida xalqaro standartlarga javob beradigan kuchli jamoani shakllantirishga asoslanadi.": "Философия нашей компании основана на формировании сильной команды на IT-рынке Узбекистана, соответствующей международным стандартам.",
    "Biz yosh dasturchilar uchun o'sish va rasmiy ishga joylashish imkoniyatini yaratamiz, bizneslar IT infratuzilmasini rivojlantiramiz va AURA Group'ni IT jahon sahnasida tanilgan kompaniyaga aylantirishni maqsad qilganmiz.": "Мы создаем возможности роста и официального трудоустройства для молодых разработчиков, развиваем IT-инфраструктуру бизнеса и стремимся сделать AURA Group узнаваемой компанией на глобальной IT-сцене.",
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

out = []
updated = 0
for block in blocks:
    lines = block.splitlines()
    if not lines or any(l.startswith("#~") for l in lines):
        out.append(block)
        continue

    msgid = ""
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
            i += 1
            while i < len(lines) and lines[i].startswith('"'):
                i += 1
            msgstr_end = i - 1
            break
        i += 1

    if msgid in mapping and msgstr_start is not None:
        lines = lines[:msgstr_start] + [f'msgstr "{esc(mapping[msgid])}"'] + lines[msgstr_end + 1 :]
        updated += 1

    out.append("\n".join(lines))

path.write_text("\n\n".join(out) + "\n", encoding="utf-8")
print(f"updated={updated}")
