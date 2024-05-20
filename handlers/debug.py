from telegram import Update
from telegram.ext import CallbackContext

def debug_stop(update: Update, context: CallbackContext) -> None:
    """Detiene el bot por emergencia"""
    update.message.reply_text("Bot detenido por emergencia. ¡Hasta luego!")
    context.bot_data['updater'].stop()
    context.bot_data['updater'].is_idle = False
