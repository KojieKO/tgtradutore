from telegram import Update
from telegram.ext import CallbackContext
from googletrans import LANGUAGES

def set_language(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if context.args:
        lang_code = context.args[0]
        if lang_code in LANGUAGES:
            context.user_data['config'] = {'language': lang_code}
            update.message.reply_text(f'Idioma de destino cambiado a {LANGUAGES[lang_code]} ({lang_code})')
        else:
            update.message.reply_text('Código de idioma no válido. Usa un código de idioma válido.')
    else:
        update.message.reply_text('Uso: /setlang <código de idioma>')
