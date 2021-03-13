import random
import re

prefix = '&'



goblin = [
	'Goblin',
	'Bugbear',
	'Shamman'
	]


async def encounters(message):
	
	command = message.content[len(prefix):].split(' ')
	
	parameters = command[1:]
	
	command = command[0]
	
	mob = ''
	
	x = 0
	
	try:
		
		if parameters[0] == 'goblin':
			
			try:
				
				level = int(parameters[1])
				
				while x < level:
					
					mob += random.choice(goblin) + ' '
					
					x += 1

				output = ''

				for y in range(len(goblin)):

					output += goblin[y] + ' : ' + str(len(re.findall(goblin[y], mob))) + '\n'
				
				await message.reply(output)
				
			except IndexError:
				
				await message.reply('Try the command again, but remember to include the desired number of creatures!')
			
	except IndexError:
		
		await message.reply('I can currently give you random encounters using the key words:')
