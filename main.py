import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Obtener el token desde las variables de entorno
TOKEN = os.getenv("BOT_TOKEN")

# Verificar si el token está definido
if not TOKEN:
    print("❌ Error: BOT_TOKEN no está definido en las variables de entorno.")
    exit(1)

# Comando /start
def start(update, context):
    update.message.reply_text("¡Hola! El bot está funcionando con la versión 13.15.")

# Respuesta tipo eco
def echo(update, context):
    texto = update.message.text
    update.message.reply_text(f"Me dijiste: {texto}")

# Manejador de errores
def error(update, context):
    print(f"⚠️ Ocurrió un error: {context.error}")

# Función principal
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Agregar manejadores
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_error_handler(error)

    print("✅ Bot conectado. Escribe /start en Telegram.")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
