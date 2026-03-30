import os
import re
import glob

def fix_html_files():
    files = glob.glob('templates/*.html')
    for fp in files:
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # O'rash xatolarini to'g'rilash: {% trans "{% trans "Text" %}" %}
        content = content.replace('{% trans "{% trans "', '{% trans "')
        content = content.replace('" %}" %}', '" %}')
        
        # Agar yana boshqa xatolar bo'lsa:
        content = re.sub(r'\{%\s*trans\s*\"\{%\s*trans\s*\"(.*?)\"\s*%\}\"\s*%\}', r'{% trans "\1" %}', content)
        
        # Oxirida ortiqcha qolib ketgan qo'shtirnoq: {% trans "Tajribali jamoa" %}"
        content = content.replace('%}"</h4>', '%}</h4>')
        content = content.replace('%}"</p>', '%}</p>')
        
        # Noto'g'ri ortiqcha belgilar
        content = content.replace('{% trans "Tajribali jamoa" %}"', '{% trans "Tajribali jamoa" %}')

        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    fix_html_files()
    print("ALL FIXED")
