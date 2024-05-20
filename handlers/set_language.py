from telegram import Update
from telegram.ext import CallbackContext

def set_language(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) != 1:
        update.message.reply_text('Usage: /setlang <language name>')
        return
    
    language_name = args[0].lower()
    context.user_data['config'] = {'input_language': language_name}
    update.message.reply_text(f'Idioma configurado: {language_name}')