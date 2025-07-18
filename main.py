import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

sinyal_keyboard = [
    ["BUY ✅", "SELL ❌"],
    ["Rejection 🔄", "Trend Lanjut 🔁"],
    ["Gold (XAUUSD)", "EUR/USD"],
    ["Bitcoin (BTCUSD)"],
]

markup = ReplyKeyboardMarkup(sinyal_keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text("Selamat datang Admin, silakan kirim sinyal trading manual kamu:", reply_markup=markup)
    else:
        await update.message.reply_text("Maaf, bot ini hanya untuk Admin.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        msg = update.message.text
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"📡 Sinyal Trading:
{msg}")
    else:
        await update.message.reply_text("Anda tidak diizinkan menggunakan bot ini.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()