import discord
from discord.mentions import AllowedMentions
import env

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.dm_messages = True
intents.guild_messages = True
intents.guilds = True
intents.members = True
allowed_mentions = AllowedMentions(users=True)

class SwearAwayBot(discord.Client):
	async def on_ready(self):
		print(f'Logged in as {bot.user.name}')
	
	async def on_message(self, message: discord.Message):
		# Prevent the bot from responding to its own messages
		if message.author == bot.user:
			return

		if "fuck" in message.content.lower():
			await message.delete()
			await message.channel.send(prettify_message(message.author.mention, message.content.replace("fuck", "flower")), allowed_mentions=allowed_mentions)

def prettify_message(author_name: str, message: str):
	return f"{author_name}:\n\"{message}\""

bot = SwearAwayBot(intents=intents)
bot.run(env.BOT_TOKEN)
