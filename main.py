from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8527276384:AAFXvihlZAgsGeSt03wErD6x2LMSGxyRaQc"

def start(update, context):
    update.message.reply_text("¡Hola! El bot está funcionando con la versión 13.15.")

def echo(update, context):
    texto = update.message.text
    update.message.reply_text(f"Me dijiste: {texto}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    print("Bot conectado. Escribe /start en Telegram.")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()