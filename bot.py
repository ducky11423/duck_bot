# bot.py - entry point

# discord imports
import discord
from discord.ext import commands

# misc imports
import sys
import json
import os

config = {}
try:
    f = open(os.path.dirname(os.path.realpath(__file__)) + "/config.json", 'r')
    config = json.load(f)
    f.close()
except:
    print("Failed to load config. Run setup.py to create config file, if config file exists ensure it is a valid JSON")
    sys.exit()

bot = commands.Bot(command_prefix='quack ')

@bot.event
async def on_ready():
    print(f"Connected as {bot.user.name} - {bot.user.id}")

if __name__ == "__main__":
    # load extensions
    bot.load_extension('util')

    bot.run(config["bot_token"], bot=True, reconnect=True)