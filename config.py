import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")

CHANNELS = {
    "jacqueline": {
        "price": os.environ.get("MODEL_1_PRICE"),
        "chat_id": os.environ.get("MODEL_1_GROUP"),
        "invite_link": "https://t.me/+Uj7U0zq16BU2NTU8"
    },
    "jennifer": {
        "price": os.environ.get("MODEL_2_PRICE"),
        "chat_id": os.environ.get("MODEL_2_GROUP"),
        "invite_link": "https://t.me/+TOSx4VygAQExNjQ0"
    }
}

