from telegram import Update
from telegram.ext import CallbackContext
import requests
import os

GITHUB_REPO = os.getenv('REPO')
GITHUB_TOKEN = os.getenv('GH_TOKEN')

def cancel_workflow_run():
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
                run_id = workflow['id']
                cancel_url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/runs/{run_id}/cancel"
                cancel_response = requests.post(cancel_url, headers=headers)
                if cancel_response.status_code == 202:
                    with open("stop_command_received.txt", "w") as f:
                        f.write("true")
                    return True
                else:
                    print(f"Error al cancelar el workflow {run_id}: {cancel_response.status_code}")
    else:
        print(f"Error al obtener los workflows: {response.status_code}")
    return False

def debug_stop(update: Update, context: CallbackContext) -> None:
    """Detiene el bot por emergencia y cancela el workflow"""
    update.message.reply_text("Bot detenido por emergencia. ¡Hasta luego!")
    context.bot_data['updater'].stop()
    context.bot_data['updater'].is_idle = False
    if cancel_workflow_run():
        update.message.reply_text("Workflow cancelado con éxito.")
    else:
        update.message.reply_text("No se pudo cancelar el workflow o no había ningún workflow en progreso.")
