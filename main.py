import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is logged in')

@client.event
async def on_message(message):
    if (message.author == client.user):
        return

    if (message.content.startswith('$disturbe')):
        image = (
            """
            https://pyxis.nymag.com/v1/imgs/392/b88/f2cae65a3354b4fc3a9ff4da05bd9821e7-31-birthday-boy.rsquare.w700.jpg
            """
        )
        for i in range(5):
            await message.channel.send(image)

    if (message.content.startswith('$clean')):
        content = (
            """
            https://www.youtube.com/watch?v=fCQufN8Wsgc
            """
        )
        for i in range(5):
            await message.channel.send(content)

    if (message.content.startswith('$sing')):
        content = (
            """
            -play https://www.youtube.com/watch?v=kVpv8-5XWOI
            """
        )
        for i in range(5):
            await message.channel.send(content)

    

client.run(TOKEN)