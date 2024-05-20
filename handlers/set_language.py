from telegram import Update
from telegram.ext import CallbackContext
from googletrans import LANGUAGES

# Diccionario adicional para símbolos
LANG_SYMBOLS = {
    'es': 'español',
    'en': 'inglés',
    '🇪🇸': 'español',
    '🇬🇧': 'inglés',
    '🇺🇸': 'inglés',
}

def set_language(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if context.args:
        lang_code = context.args[0].lower()
        lang_name = LANG_SYMBOLS.get(lang_code, LANGUAGES.get(lang_code))
        if lang_name:
            context.user_data['config'] = {'language': lang_code}
            update.message.reply_text(f'Idioma de destino cambiado a {lang_name}')
        else:
            update.message.reply_text('Código de idioma no válido. Usa un código de idioma válido.')
    else:
        update.message.reply_text('Uso: /setlang <código de idioma>')
