import os
import discord
from discord.ext import commands
from dotinv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="y!",intents=intents)

async def load_cogs():
    for filename in os.listdir("./src"):
        if filename.endwith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"[YUYUTO_SYSTEMS] {filename} is loaded.")

@bot.event
async def on_ready():
    print(f"[YUYUTO_SYSTEMS] Logged in as {bot.user.name}")
    print("---------------------------------")
    await load_cogs()
    print("[YUYUTO_SYSTEMS] All cogs loaded.")

@bot.event
async def on_connect():
    try:
        synced = await bot.tree.sync()
        print(f"[YUYUTO_SYSTEMS] Synced {len(synced)} commands.")
    except Exception as e:
        print(f"[ERROR][YUYUTO_SYSTEM] Failed to sync commands: {e}") 

if __name__ == "__main__":
    bot.run(TOKEN)