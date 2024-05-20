import os
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator
import logging

# Habilita el registro
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Crea una instancia del traductor
translator = Translator()

# Diccionario para almacenar el último idioma de cada usuario
user_language = {}

# Define los comandos iniciales
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('¡Hola! Envíame cualquier mensaje y te lo traduciré al español.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Envíame cualquier mensaje y te lo traduciré al español.')

# Función para manejar mensajes
def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    text = update.message.text

    # Si es una respuesta a un mensaje traducido, traduce en el último idioma usado
    if update.message.reply_to_message and user_id in user_language:
        target_language = user_language[user_id]
    else:
        target_language = 'es'
    
    # Traduce el mensaje
    translated = translator.translate(text, dest=target_language).text

    # Guarda el último idioma usado por el usuario
    user_language[user_id] = 'es' if target_language == 'es' else translator.detect(text).lang

    # Responde con la traducción
    update.message.reply_text(translated)

def main() -> None:
    # Leer el token del bot desde las variables de entorno
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        logger.error("No se encontró el token de Telegram. Asegúrate de que la variable de entorno TELEGRAM_TOKEN está configurada.")
        return

    updater = Updater(token)

    dispatcher = updater.dispatcher

    # Comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Mensajes
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Inicia el bot
    updater.start_polling()

    # Corre el bot hasta que se presione Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
