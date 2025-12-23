import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("8459906106:AAGMQJQ3o1Qy-_RQZ0tqF8bMEmTSxxYN_Uw")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ وصلتني رسالتك")

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN not found in environment variables")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()

if __name__ == "__main__":
    main()
