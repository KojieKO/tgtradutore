from telegram.ext import CommandHandler, MessageHandler, Filters
from .start import start
from .help import help_command
from .set_language import set_language
from .detect_language import detect_language
from .menu_handlers import show_main_menu, handle_menu, handle_language_settings
from .debug import debug_stop
from googletrans import Translator
import logging

translator = Translator()

def handle_message(update, context) -> None:
    user_id = update.message.from_user.id
    text = update.message.text
    user_config = context.user_data.get('config')
    if not user_config:
        update.message.reply_text("Please set your default input language with /setlang <language name> first.")
        return

    input_language = user_config.get('input_language')
    last_detected_language = context.user_data.get('last_detected_language', input_language)
    output_language = 'en'  # Default output language

    try:
        detected_lang = detect_language(text)
        if not detected_lang:
            raise ValueError("No se pudo detectar el idioma del mensaje.")
        
        # If the message is in the user's input language, translate to the last detected language
        if detected_lang == input_language:
            translated = translator.translate(text, dest=last_detected_language).text
        else:
            # Update the last detected language and translate to the input language
            context.user_data['last_detected_language'] = detected_lang
            translated = translator.translate(text, dest=input_language).text
        
        update.message.reply_text(translated)
    except Exception as e:
        logging.error(f"Error al traducir el mensaje: {e}")
        update.message.reply_text("Ocurrió un error al traducir el mensaje.")

def setup_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("setlang", set_language))
    dispatcher.add_handler(CommandHandler("debug_stop", debug_stop))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
