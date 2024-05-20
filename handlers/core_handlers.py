from telegram.ext import CommandHandler, MessageHandler, Filters
from .set_language import set_language
from .detect_language import detect_language
from googletrans import Translator
import logging

translator = Translator()
user_language = {}

def start(update, context) -> None:
    update.message.reply_text('¡Hola! Envíame cualquier mensaje y te lo traduciré al español.')

def help_command(update, context) -> None:
    update.message.reply_text('Envíame cualquier mensaje y te lo traduciré al español. Usa /setlang <código de idioma> para cambiar el idioma de destino.')

def handle_message(update, context) -> None:
    user_id = update.message.from_user.id
    text = update.message.text
    target_language = user_language.get(user_id, 'es')

    try:
        translated = translator.translate(text, dest=target_language).text
        update.message.reply_text(translated)
    except Exception as e:
        logging.error(f"Error al traducir el mensaje: {e}")
        update.message.reply_text("Ocurrió un error al traducir el mensaje.")

def setup_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("setlang", set_language))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
