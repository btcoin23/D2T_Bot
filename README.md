# D2T-msg-forward using Self-Bot

This is a simple Python script that forwards messages from a Discord channel to a Telegram channel when a message includes a Solana token address.
This is a **self-bot**.

https://github.com/user-attachments/assets/b36c8258-cb1c-416f-be5e-98b17236039e

## Main Features

- Forward messages from a Discord channel to a Telegram channel.
- Forward DM

## Screenshots

- Server, Channel message forward
  ![image](https://github.com/user-attachments/assets/bc82567b-85fd-49f9-a598-07a8e547bb2f)
  ![image](https://github.com/user-attachments/assets/615e58f0-ade7-4fe4-8a03-dda859500425)

- Direct message forward
  ![image](https://github.com/user-attachments/assets/5c643033-ca7d-4697-a4b1-2bf08c1e4ac6)
  ![image](https://github.com/user-attachments/assets/32a08072-eb75-460a-ac91-8f7251917fe0)

## Tech stack

- Python
- Discord Self-bot
- Discord.py
- telegram.py
- telegramify_markdown

## Prerequisites

- Python 3.13.0 or higher
- Telegram bot
- Telegram channel

## Configuration

1. clone the repository:

```
https://github.com/Any-bot/D2T-msg-forward.git
```

2. Go to the project directory:

```
cd D2T-msg-forward
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
