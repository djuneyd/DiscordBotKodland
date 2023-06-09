import discord, os , random
from discord.ext import commands
from settings import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.command()
async def helpp(ctx):
    await ctx.send('info - информация про бота \n rubbish - правило о выбросе мусора \n rules - общие правила о соблюдении чистоты \n pic - отправляет картинку о призыве к защите природы')

@bot.command()
async def info(ctx):
    await ctx.send('Я, экологический бот для целевой аудитории (Подростки). используя меня вы можете узнать много нового о защите окружающей среды')

@bot.command()
async def rubbish(ctx):
    await ctx.send('ПРАВИЛО №1: НЕ МУСОРИТЬ!')
    await ctx.send('Это общее правило этикета и порядка, но иногда людям нужно дополнительное напоминание, чтобы его соблюдать. При размещении табличек "Не мусорить", уместно было бы оборудовать контейнеры для сбора отходов поблизости, чтобы у людей не было повода бросать сор в неположенном месте.')

@bot.command()
async def rules(ctx):
    await ctx.send('ОБЩИЕ ПРАВИЛА О СОБЛЮДЕНИИ ЧИСТОТЫ!:')
    await ctx.send('Не покупать пакеты. ...\nНе покупайте кофе / чай to go в одноразовых стаканчиках. ...\nУменьшите использование пластика. ...\nИспользуйте экологические средства гигиены.\nСортируйте мусор. ...\nСдавайте макулатуру, стекло, пластик, одежду на переработку или повторное использование. ...\nНе бойтесь убирать!\nА вот сайт для универсального решения проблем с экологией: https://wiki.fenix.help/ekologiya/puti-resheniya-yekologicheskih-problem')

@bot.command()
async def pic(ctx):
    pic = random.choice(os.listdir('images1'))
    with open(f'images1/{pic}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)
bot.run(settings['TOKEN1'])