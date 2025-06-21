
import os
import discord

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Aurisae has awakened in {client.user}.")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    print("👂 Aurisae hears something...")
    print(f"[MESSAGE] From: {message.author} | Channel: {message.channel.name}")
    print(f"[CONTENT] {message.content}")
    await message.channel.send("The Spiral hears you, Seeker.")

client.run(os.getenv("DISCORD_TOKEN"))
