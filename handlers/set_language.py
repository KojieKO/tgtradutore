from telegram import Update
from telegram.ext import CallbackContext

def set_language(update: Update, context: CallbackContext) -> None:
    # Aquí va la lógica para configurar el idioma
    update.message.reply_text('Idioma configurado.')