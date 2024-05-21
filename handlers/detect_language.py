from googletrans import Translator

translator = Translator()

def detect_language(text: str) -> str:
    try:
        return translator.detect(text).lang
    except Exception as e:
        return None
