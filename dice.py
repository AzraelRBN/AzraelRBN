import re
import discord
import random

prefix = '&'

async def roll(message):

	command = message.content[len(prefix):].split(" ")

	parameters = command[1:]

	command = command[0]

	if command.lower() == 'roll':

			print(parameters)

			if len(parameters) == 0:

							await message.reply('You got a ' + str(random.randint(1,20)))

			else:
				
				dice = parameters[0].split('d')

				# modifier = parameters[1].split('+')

				numOfDice = dice[0]

				sidesOfDice = dice[1]

				print(dice)

				x = 0
				xA = 0
				xD = 0
				addition = "["
				total = 0
				additionA = "["
				additionD = "["
				totalA = 0
				totalD = 0

				while x < int(numOfDice):

					y = random.randint(1, int(sidesOfDice))

					addition += " " + str(y) + " "
					
					if x < int(numOfDice) - 1:
						
						addition += "+"

					else:

						addition += "]"

					total += y
					
					x += 1

				try:

					if parameters[1] == "+":

						addition += " + " + str(parameters[2])

						total += int(parameters[2])

					elif parameters[1] == "-":

						addition += " - " + str(parameters[2])
						
						total -= int(parameters[2])

				except IndexError:
					
					while x < int(numOfDice):

						y = random.randint(1, int(sidesOfDice))

						addition += " " + str(y) + " "
						
						if x < int(numOfDice) - 1:
							
							addition += "+"

						else:

							addition += "]"

						total += y
						
						x += 1

				output = str(addition) + " = " + str(total)

				if re.search('a', message.content, re.IGNORECASE):

					while xA < int(numOfDice):

						yA = random.randint(1, int(sidesOfDice))

						additionA += " " + str(yA) + " "
						
						if xA < int(numOfDice) - 1:
							
							additionA += "+"

						else:

							additionA += "]"

						totalA += yA
						
						xA += 1
					
					try:

						if parameters[1] == "+":

							additionA += " + " + str(parameters[2])

							totalA += int(parameters[2])

						elif parameters[1] == "-":

							additionA += " - " + str(parameters[2])
							
							totalA -= int(parameters[2])

					except IndexError:

						while xA < int(numOfDice):

							yA = random.randint(1, int(sidesOfDice))

							additionA += " " + str(yA) + " "
							
							if xA < int(numOfDice) - 1:
								
								additionA += "+"

							else:

								additionA += "]"

							totalA += yA
							
							xA += 1

					output += "\n" + str(additionA) + " = " + str(totalA)

					if total > totalA:

						output += "\n Advantage gives you a roll of " + str(total)

					elif totalA > total:

						output += "\n Advantage gives you a roll of " + str(totalA)

					elif total == totalA:

						output += "\n Lmao, both rolls got the same. With or without advantage, you got a roll of " + str(total)

				if re.search('dis', message.content, re.IGNORECASE):

					while xD < int(numOfDice):

						yD = random.randint(1, int(sidesOfDice))

						additionD += " " + str(yD) + " "
						
						if xD < int(numOfDice) - 1:
							
							additionD += "+"

						else:

							additionD += "]"

						totalD += yD
						
						xD += 1
					
					try:

						if parameters[1] == "+":

							additionD += " + " + str(parameters[2])

							totalD += int(parameters[2])

						elif parameters[1] == "-":

							additionD += " - " + str(parameters[2])
							
							totalD -= int(parameters[2])

					except IndexError:

						while xD < int(numOfDice):

							yD = random.randint(1, int(sidesOfDice))

							additionD += " " + str(yD) + " "
							
							if xD < int(numOfDice) - 1:
								
								additionD += "+"

							else:

								additionD += "]"

							totalD += yD
							
							xD += 1

					output += "\n" + str(additionD) + " = " + str(totalD)

					if total < totalD:

						output += "\n Disadvantage gives you a roll of " + str(total)

					elif totalD < total:

						output += "\n Disadvantage gives you a roll of " + str(totalD)

					elif total == totalD:

						output += "\n Lmao, both rolls got the same. With or without disadvantage, you got a roll of " + str(total)

				await message.reply(output)
