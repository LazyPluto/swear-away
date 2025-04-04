import discord
from discord.mentions import AllowedMentions
from flask import Flask
from threading import Thread
import dotenv
import os
import genai_censor

dotenv.load_dotenv()

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
		print(f"Logged in as {self.user.name}")

	async def on_raw_message_edit(self, event: discord.RawMessageUpdateEvent):
		message = event.message
		if should_censor(message.content):
			await message.delete()

			censored_message = await censor_message(message.content)
			formatted_message = prettify_message(message.author.mention, censored_message)

			print(f"Censoring message '{message.content}' with '{censored_message}'")

			await message.channel.send(formatted_message, allowed_mentions=allowed_mentions)

	async def on_message(self, message: discord.Message):
		if message.author == self.user:
			return

		if should_censor(message.content):
			await message.delete()

			censored_message = await censor_message(message.content)
			formatted_message = prettify_message(message.author.mention, censored_message)

			print(f"Censoring message '{message.content}' with '{censored_message}'")

			await message.channel.send(formatted_message, allowed_mentions=allowed_mentions)


def prettify_message(author_name: str, message: str) -> str:
	return f'{author_name}:\n"{message}"'


def should_censor(message: str) -> bool:
	message = message.lower()
	for word in swear_words:
		if word in message:
			return True
	return False


async def censor_message(message: str) -> str:
	return await genai_censor.censor(message)


app = Flask(__name__)


@app.route("/")
def status():
	return "Bot is running!"


port = int(os.getenv("PORT", "5000"))
flask_thread = Thread(target=lambda: app.run(host="0.0.0.0", port=port))
flask_thread.daemon = True
flask_thread.start()

print(f"Censoring words: {swear_words}")
bot = SwearAwayBot(intents=intents)
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
