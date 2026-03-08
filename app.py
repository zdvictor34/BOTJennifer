import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

STRIPE_LINK = "https://buy.stripe.com/6oUcN53tg0AI4wKbxycV202"

# Guardamos los usuarios que usan el bot
user_ids = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    user_ids[user_id] = True

    keyboard = [
        [InlineKeyboardButton("🔥 Unlock VIP Access", url=STRIPE_LINK)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to Jennifer's private VIP chat\n\n"
        "To access all exclusive content, please purchase VIP access below:",
        reply_markup=reply_markup
    )


async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🔥 Unlock VIP Access", url=STRIPE_LINK)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "💎 VIP Access Required\n\n"
        "Click the button below to unlock full content:",
        reply_markup=reply_markup
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("vip", vip))

    print("BOT DE JENNIFER INICIADO")

    app.run_polling()


if __name__ == "__main__":
    main()
