import telebot

# Token dan ID Telegram kamu
BOT_TOKEN = "7728622594:AAHKgMawTtzp_Sq3c_pneOR_7VgBC0Keki4"
ADMIN_ID = 7571448933

bot = telebot.TeleBot(BOT_TOKEN)

# Pesan saat /start ditekan
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id == ADMIN_ID:
        bot.reply_to(message, "✅ Halo Admin! Bot sinyal sudah aktif dan siap digunakan.")
    else:
        bot.reply_to(message, "❌ Maaf, Anda tidak memiliki akses ke bot ini.")

# Contoh fitur sinyal manual
@bot.message_handler(commands=['sinyal'])
def send_signal(message):
    if message.chat.id == ADMIN_ID:
        bot.send_message(message.chat.id, "📡 Sinyal Trading Terkini:\n\nPair: XAU/USD (Gold)\nTimeframe: M15\nArah: 🔼 BUY\nKonfirmasi: Rejection + Demand Zone\n\nGunakan manajemen risiko!")

# Menjalankan bot
bot.polling()
