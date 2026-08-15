from telegram.ext import ApplicationBuilder, MessageHandler, filters
import os

TOKEN = os.environ.get("8942289190:AAFaylYUr3ySiUUCntptfXdTz8TcFCM7JRs")

async def reply(update, context):
    if update.message and update.message.text:
        await update.message.reply_text(update.message.text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, reply))
app.run_polling()
