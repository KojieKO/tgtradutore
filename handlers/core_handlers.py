from telegram.ext import CommandHandler, MessageHandler, Filters
from .start import start
from .set_language import set_language
from .detect_language import detect_language
from .menu_handlers import show_main_menu, handle_menu, handle_language_settings
from googletrans import Translator
import logging

translator = Translator()

def handle_message(update, context) -> None:
    user_id = update.message.from_user.id
    text = update.message.text
    user_config = context.user_data.get('config')
    if not user_config:
        update.message.reply_text("Please set your default input language with /setlang <language code> first.")
        return

    input_language = user_config.get('input_language', 'es')
    output_language = user_config.get('output_language', 'en')

    try:
        detected_lang = detect_language(text)
        if detected_lang == input_language:
            translated = translator.translate(text, dest=output_language).text
        else:
            translated = translator.translate(text, dest=input_language).text
        update.message.reply_text(translated)
    except Exception as e:
        logging.error(f"Error al traducir el mensaje: {e}")
        update.message.reply_text("Ocurrió un error al traducir el mensaje.")

def setup_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("setlang", set_language))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
