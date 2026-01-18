from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import config

app = Flask(__name__)

# Crear bot AQUÍ (no en config)
bot = Bot(token=config.TELEGRAM_TOKEN)

dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

# ---------- Handlers ----------

def start(update, context):
    update.message.reply_text("✅ Bot activo por webhook en Railway")

dispatcher.add_handler(CommandHandler("start", start))

# ---------- Webhook ----------

@app.route(config.WEBHOOK_PATH, methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

# ---------- Health check ----------

@app.route("/")
def index():
    return "Bot funcionando 🚀", 200

# ---------- Run ----------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

