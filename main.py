import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is logged in')

@client.event
async def on_message(message):
    if (message.author == client.user):
        return


    if (message.content.startswith('$sanitize')):
        content = (
            """
            https://www.gannett-cdn.com/presto/2020/07/14/USAT/06a4c218-8621-48f6-8e13-95dd2f0e414e-lysol-spray-hero.jpg
            """
        )

        await message.channel.send(content)

    if (message.content.startswith('$sing')):
        content = (
            """
            -play https://www.youtube.com/watch?v=kVpv8-5XWOI
            """
        )

        await message.channel.send(content)

    

client.run(TOKEN)