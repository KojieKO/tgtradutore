from telegram import Update
from telegram.ext import CallbackContext

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Envíame cualquier mensaje y te lo traduciré al idioma configurado.')
