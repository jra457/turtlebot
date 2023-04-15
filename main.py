import os
import discord
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(
        f"Message: {message.content}\nUser: {message.author}\nChannel: #{message.channel}"
    )

    await bot.process_commands(message)

@bot.command()
async def import_turtle(ctx):
    if ctx.channel.name == 'test':
        role = get(ctx.guild.roles, name="Turtle")
        if role is None:
            role = await ctx.guild.create_role(name="Turtle")
        await ctx.author.add_roles(role)

bot.run(os.environ["TOKEN"])
