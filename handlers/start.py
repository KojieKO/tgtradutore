import os
import requests
from telegram import Update
from telegram.ext import CallbackContext

GITHUB_REPO = "username/repo"
GITHUB_TOKEN = os.getenv('GH_TOKEN')  # Obtener el token de las variables de entorno

def trigger_github_action():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/dispatches"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "event_type": "start_bot",
        "client_payload": {}
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 204

def start(update: Update, context: CallbackContext) -> None:
    if trigger_github_action():
        update.message.reply_text("Bot started successfully!")
    else:
        update.message.reply_text("Failed to start the bot.")
