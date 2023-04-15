import os
import discord
from discord.ext import commands
from discord.utils import get

# Setting up the necessary intents for the bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# Create a bot instance with the specified command prefix and intents
bot = commands.Bot(command_prefix="$", intents=intents)

# An event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

# A command that triggers when a user types "$turtle"
@bot.command(name="turtle")
async def turtle_command(ctx):
    # Send a turtle emoji as a response to the command
    await ctx.send("🐢")

# A command that triggers when a user types "$import <module_name>"
@bot.command(name="import")
async def import_module(ctx, module_name: str):
    # Check if the module name is "turtle" (case insensitive)
    if module_name.lower() == "turtle":
        # Assign the Turtle role to the user
        role = discord.utils.get(ctx.guild.roles, name="Turtle")
        
        # Create the Turtle role if it doesn't exist
        if role is None:
            role = await ctx.guild.create_role(name="Turtle")
        
        # Add the Turtle role to the user
        await ctx.author.add_roles(role)
        
        # Send a message to the chat indicating the module has been imported
        await ctx.send("Turtle module has been imported.")

# Start the bot using the provided token
bot.run(os.environ["TOKEN"])
