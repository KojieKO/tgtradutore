from telegram import Update
from telegram.ext import CallbackContext

def debug_stop(update: Update, context: CallbackContext) -> None:
    """Detiene el bot por emergencia"""
    update.message.reply_text("Bot detenido por emergencia. ¡Hasta luego!")
    updater = context.bot.updater
    updater.stop()
    updater.is_idle = False