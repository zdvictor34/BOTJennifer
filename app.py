import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

PAYMENT_LINK = "https://TU_LINK_DE_PAGO"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    args = context.args

    keyboard = [
        [InlineKeyboardButton("🔥 Acceder al VIP de Jennifer", url=PAYMENT_LINK)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if args and args[0] == "vip":

        await update.message.reply_text(
"""🔥 Hola, soy Jennifer

Estás a un paso de entrar a mi contenido privado 🔞

Pulsa el botón para acceder al VIP""",
        reply_markup=reply_markup
        )

    else:

        await update.message.reply_text(
"""🔥 Hola, soy Jennifer

Bienvenido a mi chat privado.

Escribe:

/VIP"""
        )


async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🔥 Acceder al VIP de Jennifer", url=PAYMENT_LINK)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Pulsa el botón para acceder:",
        reply_markup=reply_markup
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("vip", vip))

print("BOT DE JENNIFER INICIADO")

app.run_polling()
