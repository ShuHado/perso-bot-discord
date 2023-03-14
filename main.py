import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready.')
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print(f'Le préfixe est {bot.command_prefix}')


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello World!')


@bot.command(name='serverinfo', aliases=['si'])
async def serverinfo(ctx):
    print(ctx.author.name)
    text_channels = ctx.guild.text_channels
    text_channels_name = []
    text_channels_messages = []
    reaction_count = 0
    for text_channel in text_channels:
        text_channels_name.append(text_channel.name)
        messages = [message async for message in text_channel.history(limit=None)]
        print(text_channel)
        for message in messages:
            for reaction in message.reactions:
                print(reaction.me)
        #         async for user in reaction.users():
        #             print(f'{user.name}, {user.id} has reacted with {reaction.emoji}!')
        #             if reaction.emoji == '👍':
        #             if user.id == ctx.author.id:
        #                 reaction_count += 1
        # print(f'{ctx.author.name} has reacted {reaction_count} times in {text_channel}')

    await ctx.send(f'''Server Name: {ctx.guild.name}
Server ID: {ctx.guild.id}
Server Owner: {ctx.guild.owner}
Server Member Count: {ctx.guild.member_count}
Server Verification Level: {ctx.guild.verification_level}
Server Created At: {ctx.guild.created_at}
Server Features: {ctx.guild.features}
Server Description: {ctx.guild.description}
Server System Channel: {ctx.guild.system_channel}
Server Rules Channel: {ctx.guild.rules_channel}
Server Afk Timeout: {ctx.guild.afk_timeout}
Server Afk Channel: {ctx.guild.afk_channel}
Server System Channel Flags: {ctx.guild.system_channel_flags}
Server Channels: {text_channels_name}
Channels Messages: {text_channels_messages}''')

bot.run(os.getenv('TOKEN'))
