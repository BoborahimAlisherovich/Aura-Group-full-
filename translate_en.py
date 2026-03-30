import polib
from deep_translator import GoogleTranslator
import time

def translate_po():
    po_path = r"locale\en\LC_MESSAGES\django.po"
    print(f"Loading {po_path}...")
    po = polib.pofile(po_path)
    translator = GoogleTranslator(source='uz', target='en')
    
    count = 0
    total = len([e for e in po if not e.msgstr and e.msgid])
    
    for entry in po:
        if not entry.msgstr and entry.msgid:
            try:
                translated = translator.translate(entry.msgid)
                entry.msgstr = translated
                count += 1
                if count % 10 == 0:
                    print(f"Translated {count}/{total}...")
                time.sleep(0.5) # respectful sleep
            except Exception as e:
                print(f"Error translating '{entry.msgid}': {e}")
                
    po.save(po_path)
    print(f"Translation complete! Saved to {po_path}.")

if __name__ == "__main__":
    translate_po()
