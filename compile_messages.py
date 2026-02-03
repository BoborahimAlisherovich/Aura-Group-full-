import polib

languages = ['uz', 'ru', 'en']

for lang in languages:
    try:
        po = polib.pofile(f'locale/{lang}/LC_MESSAGES/django.po')
        po.save_as_mofile(f'locale/{lang}/LC_MESSAGES/django.mo')
        print(f'{lang} - compiled successfully!')
    except Exception as e:
        print(f'{lang} - error: {e}')

print("Done!")
