import discord
import config
from discord.ext import commands
from discord.ext.commands import Bot
import random
import obnova
from obnova import novost
import helpe
from helpe import helpa
import BotInfo
from BotInfo import infa
from BotInfo import version
import os

#Переменная префикса и основная и удаление хелпа
PREFIX = '='
client = commands.Bot(command_prefix = PREFIX)
client.remove_command("help")

#Ивент на ошибку
@client.event
async def on_commands_error( ):
    pass

#Хелп
@client.command( pass_context = True )
async def help( ctx ):
    emb = discord.Embed( title = 'Мои команды, Сэр.')
    emb.add_field( name = '{}clear'.format(PREFIX), value = 'Очистка сообщений.')
    emb.add_field( name = '{}user'.format(PREFIX), value = 'Информация об участнике.')
    emb.add_field( name = '{}news'.format(PREFIX), value = 'Новости бота.')
    emb.add_field( name = '{}bot_info'.format(PREFIX), value = 'Небольшая информация о боте.')
    emb.add_field( name = '{}bot_ver'.format(PREFIX), value = 'Версия бота.')
    await ctx.send ( embed = emb )

#Юзер
@client.command( pass_context = True )
async def user(ctx):
    author = ctx.message.author
    emb = discord.Embed( title = f'Участник { author.nick }.')
    emb.add_field( name = 'Имя:', value = f'{ author };')
    await ctx.send( embed = emb )

#Очистка сообщений
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def clear( ctx, amount : int ):
	await ctx.channel.purge( limit = amount )
	await ctx.send( f"Удалено { amount } сообщений." )
	
#Обновления
@client.command( pass_context = True )
async def news(ctx):
    await ctx.send('{0}'.format(novost))

#Информация о боте
@client.command( pass_context = True )
async def bot_info( ctx ):
    await ctx.send("{0}".format(infa))
    
@client.command( pass_context = True )
async def bot_ver( ctx ):
    await ctx.send("{0}".format(version))
    
#Ошибки с clear
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send( f"{ ctx.author.name }, укажите кол-во сообщений!")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send( f"{ ctx.author.name }, у вас недостаточно прав для использования данной команды.")

#Панель запуска и статус бота
@client.event
async def on_ready( ):
    print("Бот подключен!")
    await client.change_presence( status = discord.Status.online, activity = discord.Game("Python") )

#Запуск
#token = os.environ.get('BOT_TOKEN')
client.run( config.TOKEN )