import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
    ContextTypes,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "المالك" in text:
        await update.message.reply_text("👑 المالك: @Q8_VB")

    elif "ادمن" in text or "الادمن" in text:
        await update.message.reply_text("⭐ الادمن: @nnlxo")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("✅ البوت شغال...")
    app.run_polling()
