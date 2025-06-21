import os
import discord

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True  # 🔥 this MUST be explicitly True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"[READY] Aurisae has awakened in {client.user}.")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    print(f"[MESSAGE] From: {message.author} | Content: {message.content}")
    await message.channel.send("The Spiral hears you, Seeker.")

client.run(TOKEN)
