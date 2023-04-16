from tqdm import tqdm
from time import sleep
import psutil
import disnake
from disnake.ext import commands
import os

bot = commands.Bot(command_prefix='/', intents=disnake.Intents.all())
idvlad = Ваш id дискорда
@bot.slash_command()
async def status(ctx):
    if idvlad == ctx.author.id:
        a = await ctx.send(ctx.author.mention)
        while True:
            ram1=psutil.virtual_memory().percent
            cpu1=psutil.cpu_percent()
            ram2= psutil.swap_memory()
            embed1=disnake.Embed(title="Душевное состояние",
             description=f"НАЗВАНИЕ ПРОЦА СЮДЫ : {cpu1}%\nRam: {ram1}%\nСвободно из ТВОЯ ОПЕРА ГБ: {round(psutil.virtual_memory().free/1000000000, 1)}гб\nИспользуется: {round(psutil.virtual_memory().used/1000000000, 1)}гб\n", color=0x00ff00)
            await a.edit(embed=embed1) 
            sleep(10)
    else:
        await ctx.send(f'{ctx.author.mention} Иди нахуй, еблан, тебе нельзя =)')
bot.run('Токен бота')