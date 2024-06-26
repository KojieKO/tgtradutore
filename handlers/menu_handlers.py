from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

def show_main_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Iniciar", callback_data='start')],
        [InlineKeyboardButton("Configurar", callback_data='configure')],
        [InlineKeyboardButton("Volver", callback_data='back_to_main')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        update.callback_query.edit_message_text("Please choose:", reply_markup=reply_markup)
    else:
        update.message.reply_text("Please choose:", reply_markup=reply_markup)

def handle_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'start':
        user_config = context.user_data.get('config')
        if user_config is None:
            query.edit_message_text(text="Please set your default input language with /setlang <language code>.")
        else:
            query.edit_message_text(text=f"Bot iniciado con el idioma de entrada: {user_config['input_language']}")
            # Aquí puedes iniciar el proceso de traducción o cualquier otra funcionalidad inicial
    elif query.data == 'configure':
        show_configure_menu(query)
    elif query.data == 'back_to_main':
        show_main_menu(query)

def show_configure_menu(query):
    keyboard = [
        [InlineKeyboardButton("Idioma de entrada", callback_data='config_input_language')],
        [InlineKeyboardButton("Idioma de salida", callback_data='config_output_language')],
        [InlineKeyboardButton("Volver", callback_data='start')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Configurar opciones:", reply_markup=reply_markup)

def handle_language_settings(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'config_input_language':
        query.edit_message_text(text="Por favor, establece tu idioma de entrada con /setlang <código de idioma>.")
    elif query.data == 'config_output_language':
        query.edit_message_text(text="Por favor, establece tu idioma de salida con /setlang <código de idioma>.")
