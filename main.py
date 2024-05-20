import os
import logging
from telegram.ext import Updater
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

def main() -> None:
    logger.info("Iniciando el bot...")
    token = TOKEN
    if not token:
        logger.error("No se encontró el token de Telegram. Asegúrate de que la variable de entorno TELEGRAM_TOKEN está configurada.")
        return

    try:
        updater = Updater(token)
        dispatcher = updater.dispatcher

        # Almacenar el objeto updater en el contexto del bot
        dispatcher.bot_data['updater'] = updater

        # Configura los manejadores
        setup_handlers(dispatcher)

        start_bot(updater)

        # Corre el bot hasta que se presione Ctrl-C
        updater.idle()
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")

if __name__ == '__main__':
    main()
