import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from utils.utils import detect_solana_token_address, save_address, load_tracked_addresses
from logger import logger
import asyncio
from telethon import TelegramClient

# Load environment variables
load_dotenv()

# Access environment variables
DISCORD_USER_TOKEN = os.getenv('DISCORD_USER_TOKEN')
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
BOT_USERNAME = os.getenv('BOT_USERNAME')

# Initialize Discord client
discord_client = commands.Bot(command_prefix="!", self_bot=True)

# Initialize Telegram client
telegram_client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)

@discord_client.event
async def on_ready():
    logger.info(f'Logged in as {discord_client.user}')
    await telegram_client.start()

@discord_client.event
async def on_message(message):
    solana_addresses = detect_solana_token_address(message.content)
    logger.info(f"Detected Solana addresses: {solana_addresses}")

    if solana_addresses:
        tracked_addresses = load_tracked_addresses()
        
        for address in solana_addresses:
            if address not in tracked_addresses:
                tmp = f"{address}"
                await telegram_client.send_message(BOT_USERNAME, tmp)
                logger.info(f"Sent message for address: {address}")
                save_address(address)
                await asyncio.sleep(1)
            else:
                logger.info(f"Address already tracked: {address}")

# Start Telegram client before Discord
async def start_telegram():
    await telegram_client.start()
    logger.info("Telegram client started successfully")

# Run both clients
async def main():
    await start_telegram()
    await discord_client.start(DISCORD_USER_TOKEN)

# Run everything
if __name__ == "__main__":
    asyncio.run(main())