import glob

def clean_double_tags():
    files = glob.glob('templates/*.html')
    for fp in files:
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        # '{% trans "{% trans "Text" %}" %}'
        content = content.replace('{% trans "{% trans "', '{% trans "')
        content = content.replace('" %}" %}', '" %}')
        
        # '{% trans '{% trans 'Text' %}' %}'
        content = content.replace("{% trans '{% trans '", "{% trans '")
        content = content.replace("' %}' %}", "' %}")
        
        # Mixed quotes just in case
        content = content.replace('{% trans "{% trans \'', "{% trans '")
        content = content.replace('\' %}" %}', "' %}")
        
        content = content.replace('{% trans \'{% trans "', '{% trans "')
        content = content.replace('" %}\' %}', '" %}')
        
        # Double blocktranslates (if any remain)
        content = content.replace('{% blocktranslate %}{% blocktranslate %}', '{% blocktranslate %}')
        content = content.replace('{% endblocktranslate %}{% endblocktranslate %}', '{% endblocktranslate %}')

        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    clean_double_tags()
    print("Xatolar tozalandi!")
