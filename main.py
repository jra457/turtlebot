import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Add this line to enable the message content intent

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


@bot.command()  # Change the command name to 'turtle'
async def turtle(ctx):
  if ctx.channel.name != 'memes':  # Check if the command was sent in the 'test' channel
    return

  role_name = "Turtle"
  role = discord.utils.get(ctx.guild.roles, name=role_name)

  if not role:
    try:
      role = await ctx.guild.create_role(name=role_name)
      print(f"Created new role {role_name}")
    except discord.Forbidden:
      return

  if role not in ctx.author.roles:
    try:
      await ctx.author.add_roles(role)
    except discord.Forbidden:
      return


bot.run(os.environ["TOKEN"])
