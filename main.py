import discord
import os
import re
from keep_alive import keep_alive
from replit import db
from run_commands import commands

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

	if message.author == client.user:
		return
	
	if message.author.bot:
		return

	print(message.author.name.ljust(12) + ": " + message.content)

	await commands(client, message)

keep_alive()
client.run(os.getenv('TOKEN'))
