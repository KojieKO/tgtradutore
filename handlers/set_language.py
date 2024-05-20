from telegram import Update
from telegram.ext import CallbackContext
from googletrans import Translator

translator = Translator()

def set_language(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) != 1:
        update.message.reply_text('Usage: /setlang <language name>')
        return
    
    language_name = args[0].lower()
    try:
        lang_code = translator.translate('test', dest=language_name).dest
        context.user_data['config'] = {'input_language': lang_code}
        update.message.reply_text(f'Idioma configurado: {language_name}')
    except Exception as e:
        update.message.reply_text('Idioma no soportado. Por favor, use un nombre de idioma válido.')
