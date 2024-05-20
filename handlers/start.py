def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_config = context.user_data.get('config')

    if user_config is None:
        update.message.reply_text(
            "Hello! This bot will help you translate. Please set your default language with /setlang <language code>."
        )
    else:
        update.message.reply_text(
            f"Welcome back! Your default translation language is set to {user_config['language']}."
        )
