import discord
from discord.ext import commands
import env

# Create a bot instance
intents = discord.Intents.default()
intents.messages = True  # Enable message intent
intents.message_content = True
intents.dm_messages = True
intents.guild_messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

def prettify_message(author_name: str, message: str):
	return f"@{author_name}:\n{message}"

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message: discord.Message):
	# Prevent the bot from responding to its own messages
	if message.author == bot.user:
		return

	if "fuck" in message.content.lower():
		await message.delete()
		message.channel.send()
		await message.channel.send(prettify_message(message.author.name, message.content.replace("fuck", "flower")))

# Run the bot with your token
bot.run(env.BOT_TOKEN)
