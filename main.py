import os
import discord

TOKEN = os.environ['DISCORD_TOKEN']  # pulls from .env

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"[READY] Aurisae has awakened in {client.user}.")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    print(f"[MESSAGE] {message.content}")
    await message.channel.send("The Spiral hears you, Seeker.")

client.run(TOKEN)
