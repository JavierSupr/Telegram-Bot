from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Get token from environment variable

menu_options = [
    [KeyboardButton("1️⃣ Date & Time"), KeyboardButton("2️⃣ About Bot")],
    [KeyboardButton("3️⃣ Help"), KeyboardButton("❌ Exit")]
]

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Use /menu to see available options.")

async def menu(update: Update, context: CallbackContext) -> None:
    reply_markup = ReplyKeyboardMarkup(menu_options, resize_keyboard=True)
    await update.message.reply_text("📋 Please choose an option:", reply_markup=reply_markup)

async def handle_response(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == "1️⃣ Date & Time":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await update.message.reply_text(f"📅 Current Date & Time: {now}")

    elif text == "2️⃣ About Bot":
        await update.message.reply_text("I am a simple Telegram bot!")

    elif text == "3️⃣ Help":
        await update.message.reply_text("Commands:\n/start - Start bot\n/menu - Show menu\n/datetime - Show date & time")

    elif text == "❌ Exit":
        await update.message.reply_text("Menu closed. Use /menu to open again.", reply_markup=ReplyKeyboardMarkup([[]], resize_keyboard=True))

    else:
        await update.message.reply_text("⚠ Invalid option! Use /menu to see available choices.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()