import os
import requests
from telegram import Update
from telegram.ext import CallbackContext

GITHUB_REPO = "username/repo"
GITHUB_TOKEN = os.getenv('GH_TOKEN')

def get_workflow_status():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/runs"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        workflows = response.json().get('workflow_runs', [])
        for workflow in workflows:
            if workflow['status'] in ['in_progress', 'queued']:
                return True
    return False

def trigger_github_action():
    if get_workflow_status():
        return False

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
    if 'config' not in context.user_data:
        update.message.reply_text("Please set your default input language with /setlang <language name> first.")
        return
    
    if trigger_github_action():
        update.message.reply_text("Bot started successfully!")
    else:
        update.message.reply_text("Failed to start the bot or a workflow is already running.")
