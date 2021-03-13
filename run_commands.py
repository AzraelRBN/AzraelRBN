import discord
import re

from dice import roll
from spells import spells
from encounters import encounters
from hbt import hbt, templates
from help import help

global prefix
prefix = '&'

async def commands(client, message):
	
	global prefix
	if message.content.startswith(prefix):

		command = message.content[len(prefix):].split(" ")

		parameters = command[1:]

		command = command[0]

		if command.lower() == 'help':

			await help(message)

		elif command.lower() == 'roll':

			await roll(message)

		elif command.lower() == 'spell':

			await spells(message)
			
		elif command.lower() == 'monster':
			
			return
		
		elif command.lower() == 'class':
			
			return
		
		elif command.lower() == 'race':
			
			return
		
		elif command.lower() == 'deity':
			
			return
		
		elif command.lower() == 'encounter':
			
			await encounters(message)

		elif command.lower() == 'homebrew':

			await hbt(message)

		elif command.lower() == 'template':

			await templates(message)

		else:

			await message.reply("I don't recognize that command. Maybe you mispelled something?")
