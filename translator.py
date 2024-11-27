# translator.py

from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Sample usage
print(translate_text("Hello, world!", "es"))
