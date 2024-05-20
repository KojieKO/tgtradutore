import os
import logging
from telegram.ext import Updater, CommandHandler
from config import TOKEN
from handlers.core_handlers import setup_handlers

# Habilita el registro
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start_bot(updater):
    """Inicia el bot"""
    updater.start_polling()
    logger.info("Bot iniciado")

def stop_bot(update, context, updater):
    """Detiene el bot"""
    update.message.reply_text("Bot detenido. ¡Hasta luego!")
    updater.stop()
    updater.is_idle = False
    logger.info("Bot detenido")

def main() -> None:
    logger.info("Iniciando el bot...")
    token = TOKEN
    if not token:
        logger.error("No se encontró el token de Telegram. Asegúrate de que la variable de entorno TELEGRAM_TOKEN está configurada.")
        return

    try:
        updater = Updater(token)
        dispatcher = updater.dispatcher

        # Configura los manejadores
        setup_handlers(dispatcher)

        # Añadir manejador para detener el bot
        dispatcher.add_handler(CommandHandler("stop", lambda update, context: stop_bot(update, context, updater)))

        start_bot(updater)

        # Corre el bot hasta que se presione Ctrl-C
        updater.idle()
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")

if __name__ == '__main__':
    main()