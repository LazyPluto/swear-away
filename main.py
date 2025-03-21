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

with open("swear-words.txt") as f:
	swear_words = [word.strip() for word in f.readlines()]

class SwearAwayBot(discord.Client):
	async def on_ready(self):
		print(f'Logged in as {bot.user.name}')
	
	async def on_message(self, message: discord.Message):
		if message.author == bot.user:
			return

		if should_censor(message.content):
			await message.delete()
			await message.channel.send(prettify_message(message.author.mention, message.content.replace("fuck", "flower")), allowed_mentions=allowed_mentions)

def prettify_message(author_name: str, message: str):
	return f"{author_name}:\n\"{message}\""

def should_censor(message: str):
	message = message.lower()
	for word in swear_words:
		if word in message:
			return True
	return False

print(f"Censoring words: {swear_words}")
bot = SwearAwayBot(intents=intents)
bot.run(env.BOT_TOKEN)
