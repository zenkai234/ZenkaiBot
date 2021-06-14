import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix ='.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'confirm'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidely so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'Cause Zenkai says so ;)',
                 'Most likely bro.',
                 'Zenkai doubts that ^_^',
                 'Signs points to yes.',
                 'Cannot predict now man.',
                 'Reply hazy, try again my man.',
                 'Zenkai says No!',
                 'Zenkai approves!',
                 'Zenkai does not approve!',
                 'Now that is an argument between Zenkai and Merit!',
                 'That is an unpredictable question perhabs?',
                 'Stop asking that bullshit I will send a hitman after you?',
                 'Yeewah is gay! Did you expect me to answer this or was there an error in your question? Ask again I might reply differently']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run('ODUzNjk3NzUxMTI0Mjc5MzU3.YMZJ_A.yrObDIRMySjTWItmaY5rdKtzCwI')
