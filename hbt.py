import discord




prefix = '&'

async def hbt(message):

	await message.reply("If you are interested in creating some homebrew, just ask your DM! In most cases, they'll work with you to create something that will add to your game experience. Make sure to take a peak at the templates using &template (whatever you're creating)! If the template doesn't exist, don't worry. Just ask your DM for some help.")

async def templates(message):

	command = message.content[len(prefix):].split(' ')

	parameters = command[1:]

	command = command[0]

	try:

		if parameters[0].lower() == 'spell':

			embed = discord.Embed(name = "Spell Template", description = "What does your spell do?", color = 0x4f094e)

			embed.add_field(name = "At Higher Levels", value = "What does your spell do when cast at a higher level?", inline = False)

			embed.add_field(name = "Level", value = "What is the base level of your spell?", inline = True)

			embed.add_field(name = "School", value = "What school of magic does your spell belong to?", inline = True)

			embed.add_field(name = "Casting Time", value = "How long does it take to cast your spell?", inline = True)

			embed.add_field(name = "Range", value = "What is the range (n feet) of your spell?", inline = True)

			embed.add_field(name = "Components", value = "What are the required components of your spell?", inline = True)

			embed.add_field(name = "Duration", value = "How long does your spell last?", inline = True)

			embed.set_footer(text = "You DM does this part!")

			await message.reply(embed = embed)




		else:

			await message.reply("Looks like you either made a spelling error, or the template doesn't exist.")

	except IndexError:

		await message.reply('Try the command again with the template you wish to see!')
