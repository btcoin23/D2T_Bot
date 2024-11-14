# D2T-msg-forward using Self-Bot

This is a simple Python script that forwards messages from a Discord channel to a Telegram channel when a message includes a Solana token address.
This is a **self-bot**.

https://github.com/user-attachments/assets/b36c8258-cb1c-416f-be5e-98b17236039e

## Main Features

- Forward messages from a Discord channel to a Telegram channel.
- Forward DM

## Tech stack

- Python
- Discord Self-bot
- Discord.py
- telegram.py

## Prerequisites

- Python 3.13.0 or higher
- Telegram bot
- Telegram channel

## Configuration

1. clone the repository:

```
https://github.com/btcoin23/D2T_Bot
```

2. Go to the project directory:

```
cd D2T_Bot
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Create a .env file in the root directory of the project and add the following variables:

```
DISCORD_USER_TOKEN=
TELEGRAM_TOKEN=
TELEGRAM_CHANNEL_ID=
```

5. Run the script:

```
python main.py
```

## Version 1.0 13/11/2024
