import glob
import re

def clean_all_trans():
    files = glob.glob('templates/**/*.html', recursive=True)
    count = 0
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        orig_content = content
        
        # O'rash xatolari (ichma-ich teglar)
        content = re.sub(r'\{%\s*trans\s*\"\{%\s*trans\s*\"(.*?)\"\s*%\}\"\s*%\}', r'{% trans "\1" %}', content)
        content = re.sub(r'\{%\s*trans\s*\'\{%\s*trans\s*\'(.*?)\'\s*%\}\'\s*%\}', r"{% trans '\1' %}", content)
        
        # Xato o'zgaruvchi formatlari: '{% trans "{% trans "Text" %}" %}' (faqat oddiy stringlar)
        content = content.replace('{% trans "{% trans "', '{% trans "')
        content = content.replace('" %}" %}', '" %}')
        content = content.replace('{% trans \'{% trans \'', '{% trans \'')
        content = content.replace('\' %}\' %}', '\' %}')

        # Duplicate same translation block right after each other: {% trans "Text" %} {% trans "Text" %}
        # Sometimes there's whitespace or newlines.
        
        # Repeated `trans` keyword in the same tag: `{% trans trans "..." %}`
        content = re.sub(r'\{%\s*trans\s+trans\s+', '{% trans ', content)

        if content != orig_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Fixed: {f}")
            count += 1
            
    print(f"Total files fixed: {count}")

if __name__ == '__main__':
    clean_all_trans()
