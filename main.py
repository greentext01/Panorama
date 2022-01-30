import asyncio
import os
import random
from discord.ext import commands
import dotenv

dotenv.load_dotenv()

TOKEN = os.environ.get('TOKEN')
bot = commands.Bot('>_ ', self_bot=True)
fish_channel = None

@bot.event
async def on_ready():
    print('ready >:)')


@bot.event
async def on_message(message):
    global fish_channel

    if message.content == 'fish':
        if message.author.id == bot.user.id:
            fish_channel = message.channel.id
            while True:
                await message.channel.send('p!fish')
                await asyncio.sleep(62)
    elif message.author.bot and message.author.name == 'Pancake' \
            and message.author.discriminator == '3691' and message.channel.id == fish_channel:

        print(message.content)

        await asyncio.sleep(1)
        
        if 'Your fishing rod broke!' in message.content:
            await asyncio.sleep(3)
            await message.channel.send('p!buy fishing rod')
        elif 'purchase' in message.content or 'sell' in message.content:
            if message.reactions:
                await message.add_reaction(message.reactions[0])
        elif 'casted out a line...' in message.content:
            await message.channel.send('p!sell all')
            await asyncio.sleep(random.randint(80, 120))
            await message.channel.send('p!give olive 100')


bot.run(TOKEN)
