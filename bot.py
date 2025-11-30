import os
import telebot
from telebot import types
from datetime import datetime

# Get from environment variables - NEVER hardcode tokens!
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_LINK = os.environ.get('CHANNEL_LINK', 'https://t.me/YourFlightsChannel')
LOG_FILE = "users.txt"

# Check if token exists
if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN environment variable is not set!")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

def log_user(user_id, username, action="start"):
    try:
        with open(LOG_FILE, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {user_id} - {username} - {action}\n")
    except Exception as e:
        print(f"Logging error: {e}")

# ... (rest of your bot code remains the same)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"
    log_user(user_id, username, "start")

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK))
    # ... (rest of your start function)

if __name__ == "__main__":
    print("🛫 USA Flights Bot is running...")
    bot.polling(none_stop=True)