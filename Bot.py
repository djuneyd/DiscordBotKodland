from settings import settings
import discord
# import * - это тоже самое, что перечислить все файлы
from bot_logic import *

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)


# Когда бот будет готов, он напишет в консоли свое название!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Когда бот будет получать сообщение, он будет отправлять в этот же канал какие-то сообщения!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Привет! Я бот!')
    elif message.content.startswith('$help'):
        await message.channel.send('$hello - поздароваться')
        await message.channel.send('$smile - сгенерировать смайлик')
        await message.channel.send('$coin - подбросить монетку')
        await message.channel.send('$pass - сгенерировать пароль')
        await message.channel.send('$spam - заспамить')
        await message.channel.send('$greet - поздароваться по id')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$spam'):
        for i in range(100):
            await message.channel.send('spam')
            await message.channel.send('spam')
            await message.channel.send('spam')
            await message.channel.send('spam')
            await message.channel.send('spam')
    elif message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.author}!')

client.run(settings["TOKEN"])
