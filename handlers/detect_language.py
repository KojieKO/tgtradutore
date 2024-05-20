from googletrans import Translator

translator = Translator()

def detect_language(text: str) -> str:
    return translator.detect(text).lang