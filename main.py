import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from utils.utils import detect_solana_token_address, save_address, load_tracked_addresses
from logger import logger
import asyncio
from telethon import TelegramClient
import json

# Load environment variables
load_dotenv()

# Load config
def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

config = load_config()

# Access environment variables
DISCORD_USER_TOKEN = os.getenv('DISCORD_USER_TOKEN')
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')

# Get settings from config
BOT_USERNAME = config['telegram']['bot_username']
MONITORED_SERVERS = config['discord']['server_channels']

# Initialize Discord client
intents = discord.Intents.default() 
intents.message_content = True 
discord_client = commands.Bot(command_prefix="!", self_bot=True, intents=intents)


# Initialize Telegram client
telegram_client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)

@discord_client.event
async def on_ready():
    logger.info(f'Logged in as {discord_client.user}')
    await telegram_client.start()

@discord_client.event 
async def on_message(message): 
    # Check if message is from monitored server and channel 
    server_id = str(message.guild.id) 
    channel_id = str(message.channel.id) 
    for server_config in MONITORED_SERVERS: 
        if server_id in server_config: 
            if channel_id in server_config[server_id]: 
                logger.info(f"1. Detected message in monitored server and channel: {message.content}") 
                solana_addresses = detect_solana_token_address(message.content) 
                logger.info(f"2. Detected Solana addresses: {solana_addresses}") 
                if solana_addresses: 
                    logger.info(f"3. Sending message for addresses: {solana_addresses}") 
                    tracked_addresses = load_tracked_addresses() 
                    logger.info(f"4. Tracked addresses: {tracked_addresses}") 
                    for address in solana_addresses: 
                        logger.info(f"5. Checking address: {address}") 
                        if address not in tracked_addresses: 
                            logger.info(f"6. Sending message for address: {address}") 
                            tmp = f"{address}" 
                            await telegram_client.send_message(BOT_USERNAME, tmp) 
                            logger.info(f"7. Sent message for address: {address}") 
                            save_address(address) 
                            await asyncio.sleep(1) 
                        else: 
                            logger.info(f"8. Address already tracked: {address}") 
 
async def clean_files(): 
    # Clear app.log 
    open('app.log', 'w').close() 
    # Clear tracked_addresses.json 
    open('tracked_addresses.json', 'w').close() 
 
# Start Telegram client before Discord 
async def start_telegram(): 
    logger.info("Starting Telegram client...") 
    await telegram_client.start() 
    logger.info("Telegram client started successfully") 
 
# Run both clients 
async def main(): 
    logger.info("Starting D2T bot...") 
    # await clean_files() 
    await start_telegram() 
    await discord_client.start(DISCORD_USER_TOKEN) 
 
# Run everything 
if __name__ == "__main__": 
    asyncio.run(main())

# main.py