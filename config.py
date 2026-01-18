# config.py
import os

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Stripe (si lo usas)
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

# Webhook
BASE_URL = os.getenv("BASE_URL")  # https://xxxx.up.railway.app
WEBHOOK_PATH = "/telegram/webhook"
WEBHOOK_URL = f"{BASE_URL}{WEBHOOK_PATH}"

# Seguridad mínima
if not TELEGRAM_TOKEN:
    raise RuntimeError("❌ TELEGRAM_TOKEN no está definido")

