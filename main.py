import os
import logging
from telegram.ext import Updater
from config import TOKEN
from handlers.inith import setup_handlers

# Habilita el registro
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

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

        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")

if __name__ == '__main__':
    main()