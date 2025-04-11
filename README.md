# 📱 Simple Telegram Bot

A simple Telegram bot built using Python and the `python-telegram-bot` library. This bot provides a menu interface for users to get the current date & time, learn about the bot, get help, or exit the menu.

## ✨ Features

- `/start`: Greet the user and provide basic instructions.
- `/menu`: Display a custom keyboard with interactive options:
  - `1️⃣ Date & Time`: Shows the current date and time.
  - `2️⃣ About Bot`: Displays a short description of the bot.
  - `3️⃣ Help`: Lists available commands.
  - `❌ Exit`: Closes the menu.

## 📦 Requirements

- Python 3.7+
- `python-telegram-bot`
- `python-dotenv`

Install the dependencies using pip:

```bash
pip install python-telegram-bot python-dotenv
```

## ⚙️ Setup

1. Clone this repository or copy the code.

2. Create a `.env` file in the root directory:

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```

3. Run the bot:

```bash
python your_bot_script.py
```

> Replace `your_bot_script.py` with the name of your Python file.

## 🧠 How It Works

- The bot listens for `/start` and `/menu` commands.
- When `/menu` is triggered, a custom keyboard appears.
- The bot responds based on the button pressed using `handle_response()`.

## 🖼 Screenshot

_You can add a screenshot of the bot here._

## 📌 Notes

- Make sure your bot is registered with [BotFather](https://t.me/BotFather) and has the correct permissions.
- To update the menu or add more functionality, modify the `menu_options` and `handle_response` function.