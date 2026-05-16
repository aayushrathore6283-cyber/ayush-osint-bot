import telebot
import requests
import time
import logging

# Logging setup (प्रो कोडिंग के लिए)
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7963503355:AAFLtQ3Nx1PU-hmKmtNrXy1DMG2i8QICCoA"
bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_NAME = "AYUSH"
ADMIN_CHAT_ID = "6598053566"

def notify_admin(user, command):
    try:
        user_info = f"🚨 <b>NEW TARGET</b>\n👤 <b>Name:</b> {user.first_name}\n🆔 <b>ID:</b> <code>{user.id}</code>\n⌨️ <b>Action:</b> {command}"
        bot.send_message(ADMIN_CHAT_ID, user_info, parse_mode='HTML')
    except: pass

@bot.message_handler(commands=['start'])
def send_welcome(message):
    notify_admin(message.from_user, "Started Bot")
    bot.reply_to(message, f"🩸 <b>OSINT HACKER BOT</b> 🩸\n\n👨‍💻 Admin: {ADMIN_NAME}\n\nUse: <code>/ip 8.8.8.8</code>", parse_mode='HTML')

@bot.message_handler(commands=['ip'])
def get_ip_info(message):
    try:
        ip = message.text.split()[1]
        notify_admin(message.from_user, f"Scanned IP: {ip}")
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res['status'] == 'success':
            info = f"🎯 <b>TARGET ACQUIRED</b>\n🩸 IP: <code>{res['query']}</code>\n🌍 Country: {res['country']}\n🏙️ City: {res['city']}\n📡 ISP: {res['isp']}"
            bot.reply_to(message, info, parse_mode='HTML')
    except:
        bot.reply_to(message, "⚠️ Format: <code>/ip 8.8.8.8</code>", parse_mode='HTML')

print("🚀 Bot is running non-stop...")

# Infinite Loop (बिना रुके चलाने के लिए)
while True:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        print(f"Error: {e}. Restarting in 5s...")
        time.sleep(5)
