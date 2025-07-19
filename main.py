import telebot

# Token dan ID Telegram kamu
BOT_TOKEN = "7728622594:AAHKgMawTtzp_Sq3c_pneOR_7VgBC0Keki4"
ADMIN_ID = 7571448933

bot = telebot.TeleBot(BOT_TOKEN)

# Saat /start ditekan
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id == ADMIN_ID:
        bot.reply_to(message, "✅ Halo Admin! Bot sinyal sudah aktif dan siap digunakan.")
    else:
        bot.reply_to(message, "❌ Maaf, Anda tidak memiliki akses ke bot ini.")

# Sinyal manual lengkap
@bot.message_handler(commands=['sinyal'])
def send_signal(message):
    if message.chat.id == ADMIN_ID:
        signal_text = (
            "📡 Sinyal Trading Terkini:

"
            "Pair: XAU/USD (Gold)
"
            "Timeframe: M15
"
            "Arah: 🔼 BUY
"
            "Konfirmasi: Rejection + Demand Zone
"
            "Trend: Uptrend
"
            "FVG: Terisi
"
            "Volume: Spike Volume
"
            "Berita: Tidak ada berita besar saat ini

"
            "Gunakan manajemen risiko dengan bijak."
        )
        bot.send_message(message.chat.id, signal_text)

# Notifikasi setelah berita besar
@bot.message_handler(commands=['aktif'])
def aktifkan_bot(message):
    if message.chat.id == ADMIN_ID:
        bot.send_message(message.chat.id, "✅ Bot kembali aktif memberi sinyal setelah berita besar.")

# Fitur stop sementara
@bot.message_handler(commands=['stop'])
def stop_bot(message):
    if message.chat.id == ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ Bot dinonaktifkan sementara. Tunggu kondisi market lebih baik.")

# Jalankan bot
bot.polling()
