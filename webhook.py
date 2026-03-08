import stripe
from flask import Flask, request
from telegram import Bot

BOT_TOKEN = "TU_TOKEN_BOT"
GROUP_ID = -1003438427168

bot = Bot(token=BOT_TOKEN)

stripe.api_key = "TU_STRIPE_SECRET"
endpoint_secret = "whsec_9OypXLEVZpjzrPPFVbaXL9JqGqmas6gv"

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def stripe_webhook():

    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception as e:
        return str(e), 400

    if event['type'] == 'checkout.session.completed':

        session = event['data']['object']
        telegram_id = session['metadata']['telegram_id']

        invite_link = bot.create_chat_invite_link(
            chat_id=GROUP_ID,
            member_limit=1
        )

        bot.send_message(
            chat_id=telegram_id,
            text=f"💎 Payment successful!\n\nJoin the VIP group:\n{invite_link.invite_link}"
        )

    return '', 200


app.run(host="0.0.0.0", port=8080)
