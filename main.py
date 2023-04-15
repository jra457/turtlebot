import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.command(name="turtle")
async def turtle_command(ctx):
    await ctx.send("🐢")

@bot.command(name="import")
async def import_module(ctx, module_name: str):
    if module_name.lower() == "turtle":
        # Assign the Turtle role to the user
        role = discord.utils.get(ctx.guild.roles, name="Turtle")
        if role is None:
            role = await ctx.guild.create_role(name="Turtle")
        await ctx.author.add_roles(role)
        
        # Send a message to the chat
        await ctx.send("Turtle module has been imported.")

bot.run(os.environ["TOKEN"])
