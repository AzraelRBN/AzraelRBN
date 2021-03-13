import discord

commandList = [
	'roll',
	'spell',
	'encounter',
	'homebrew',
	'template',
	'info'
]

prefix = '&'

async def help(message):

	command = message.content[len(prefix):].split(' ')

	parameters = command[1:]

	command = command[0]

	try:

		if parameters[0] == 'roll':

			embed = discord.Embed(name = "Roll", color = 0x4f094e)

			embed.add_field(name = "Command", value = "&roll (x)d(y) + (z) (a/dis)", inline = False)

			embed.add_field(name = "x", value = "x is the number of dice you wish to roll.", inline = True)

			embed.add_field(name = "y", value = "y is the number of sides on the dice.", inline = True)

			embed.add_field(name = "z", value = "z is the modifier for your roll.", inline = True)

			embed.add_field(name = "a/dis", value = "Adding a to the end will roll your dice with advantage. Adding dis does the opposite.", inline = True)

			embed.add_field(name = "Example", value = "&roll 3d10 + 5 a", inline = False)

			await message.channel.send(embed = embed)

		elif parameters[0] == 'spell':

			embed = discord.Embed(name = "Spell", color = 0x4f094e)

			embed.add_field(name = "Command", value = "&spell (name of spell)", inline = False)

			embed.add_field(name = "Example", value = "&spell acid splash", inline = False)

			await message.channel.send(embed = embed)

		elif parameters[0] == 'info':

			embed = discord.Embed(name = "CelestialBot", description = "Celestial Wasteland D&D companion")

			return



		else:

			await message.reply('Make sure your spelling is correct. If that is not the issue, then it is a coding bug and you should talk to Azrael about it')

	except IndexError:

		output = '```py'

		x = -1

		while x < len(commandList):

			output += commandList[x] + '\n'

			x += 1

		output += '```'

		await message.reply('Hello! I am CelestialBot, your friendly D&D companion bot. I was created by Azrael specifically for Celestial Wasteland and their D&D games. Enough about me though. Here are those commands you are looking for!\n' + output)
