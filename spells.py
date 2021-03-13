import discord


prefix = '&'



async def spells(message):

	command = message.content[len(prefix):].split(' ')

	parameters = command[1:]

	command = command[0]

	spell = ''

	x = 0

	

	while x < len(parameters):

		spell += parameters[x]

		x += 1

	print(spell)
	
	try:

		if spell.lower() == 'acidsplash':

			embed = discord.Embed(title = "Acid Splash", url = "http://dnd5e.wikidot.com/spell:acid-splash", description = "You hurl a bubble of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.", color = 0x4f094e)

			embed.add_field(name = "At Higher Levels", value = "This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).", inline = False)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Conjuration", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "60 Feet", inline = True)

			embed.add_field(name ="Component", value = "Verbal, Somatic", inline = True)

			embed.add_field(name = "Duration", value = "Instantanious", inline = True)

			embed.set_footer(text = "Players Handbook")

			await message.reply(embed = embed)
			
		if spell.lower() == 'bladeward':
			
			embed = discord.Embed(title = "Blade Ward", url = "http://dnd5e.wikidot.com/spell:blade-ward", description = "You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon attacks.", color = 0x4f094e)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Abjuartion", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "Self", inline = True)

			embed.add_field(name ="Component", value = "Verbal, Somatic", inline = True)

			embed.add_field(name = "Duration", value = "1 Round", inline = True)

			embed.set_footer(text = "Players Handbook")
			
			await message.reply(embed = embed)
			
		if spell.lower() == 'boomingblade':
			
			embed = discord.Embed(title = "Booming Blade", url = "http://dnd5e.wikidot.com/spell:booming-blade", description = "You brandish the weapon used in the spell’s casting and make a melee attack with it against one creature within 5 feet of you. On a hit, the target suffers the weapon attack’s normal effects and then becomes sheathed in booming energy until the start of your next turn. If the target willingly moves 5 feet or more before then, the target takes 1d8 thunder damage, and the spell ends.", color = 0x4f094e)

			embed.add_field(name = "At Higher Levels", value = "At 5th level, the melee attack deals an extra 1d8 thunder damage to the target on a hit, and the damage the target takes for moving increases to 2d8. Both damage rolls increase by 1d8 at 11th level (2d8 and 3d8) and again at 17th level (3d8 and 4d8).", inline = False)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Evocation", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "Self", inline = True)

			embed.add_field(name ="Component", value = "Somatic, Material (A melee weapon worth at least 1sp)", inline = True)

			embed.add_field(name = "Duration", value = "1 Round", inline = True)

			embed.set_footer(text = "Players Handbook")
			
			await message.reply(embed = embed)
			
		if spell.lower() == 'chilltouch':
			
			embed = discord.Embed(title = "Chill Touch", url = "http://dnd5e.wikidot.com/spell:chill-touch", description = "You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can’t regain hit points until the start of your next turn. Until then, the hand clings to the target. If you hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn.", color = 0x4f094e)

			embed.add_field(name = "At Higher Levels", value = "This spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).", inline = False)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Necromancy", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "120 Feet", inline = True)

			embed.add_field(name ="Component", value = "Verbal, Somatic", inline = True)

			embed.add_field(name = "Duration", value = "1 Round", inline = True)

			embed.set_footer(text = "Players Handbook")
			
			await message.reply(embed = embed)
			
		if spell.lower() == 'controlflames':
			
			embed = discord.Embed(title = "Control Flames", url = "http://dnd5e.wikidot.com/spell:control-flames", description = "You choose nonmagical flame that you can see within range and that fits within a 5-foot cube. You affect it in one of the following ways:\n\t\t• You instantaneously expand the flame 5 feet in one direction, provided that wood or other fuel is present in the new location.\n\t\t• You instantaneously extinguish the flames within the cube.You double or halve the area of bright light and dim light cast by the flame, change its color, or both. The change lasts for 1 hour.\n\t\t• You cause simple shapes—such as the vague form of a creature, an inanimate object, or a location—to appear within the flames and animate as you like. The shapes last for 1 hour.\nIf you cast this spell multiple times, you can have up to three of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action.", color = 0x4f094e)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Transmutation", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "60 Feet", inline = True)

			embed.add_field(name ="Component", value = "Somatic", inline = True)

			embed.add_field(name = "Duration", value = "Instantaneous or 1 Hour", inline = True)

			embed.set_footer(text = "Xanathar's Guide to Everything")
			
			await message.reply(embed = embed)
			
		if spell.lower() == 'createbonfire':
			
			embed = discord.Embed(title = "Create Bonfire", url = "http://dnd5e.wikidot.com/spell:create-bonfire", description = "You create a bonfire on ground that you can see within range. Until the spell ends, the bonfire fills a 5-foot cube. Any creature in the bonfire’s space when you cast the spell must succeed on a Dexterity saving throw or take 1d8 fire damage. A creature must also make the saving throw when it enters the bonfire’s space for the first time on a turn or ends its turn there.", color = 0x4f094e)

			embed.add_field(name = "At Higher Levels", value = "The spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).", inline = False)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Conjuration", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "60 Feet", inline = True)

			embed.add_field(name ="Component", value = "Verbal, Somatic", inline = True)

			embed.add_field(name = "Duration", value = "Concentration, up to 1 Minute", inline = True)

			embed.set_footer(text = "Xanather's Guide to Eveything")
			
			await message.reply(embed = embed)
			
		if spell.lower() == 'dancinglights':
			
			embed = discord.Embed(title = "Dancing Lights", url = "http://dnd5e.wikidot.com/spell:dancing-lights", description = "You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10-foot radius. As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell’s range.", color = 0x4f094e)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Evocation", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "120 Feet", inline = True)

			embed.add_field(name ="Component", value = "Verbal, Somatic, Material (a bit of phosphorus or wychwood, or a glowworm)", inline = True)

			embed.add_field(name = "Duration", value = "Concentration, up to 1 Minute", inline = True)

			embed.set_footer(text = "Players Handbook")

			await message.reply(embed = embed)

		if spell.lower() == 'decompose':

			embed = discord.Embed(title = "Decompose", url = "http://dnd5e.wikidot.com/spell:decompose", description = "You reach out and touch the corpse of a creature. Over the next minute, the corpse begins to rapidly decompose, sprouting fungus and moss as it begins to degrade into compost and mulch. An odd-colored flower or two may also spring from the corpse in this time. Applicable requirements for resurrection are unaffected by this decomposition.", color = 0x4f094e)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Necromancy", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "Touch", inline = True)

			embed.add_field(name ="Component", value = "Verbal, Somatic", inline = True)

			embed.add_field(name = "Duration", value = "1 Minute", inline = True)

			embed.set_footer(text = "Homebrew: Critical Role")

			await message.reply(embed = embed)

		if spell.lower() == 'druidcraft':

			embed = discord.Embed(title = "Druidcraft", url = "http://dnd5e.wikidot.com/spell:druidcraft", description = "Whispering to the spirits of nature, you create one of the following effects within range:\n\t\t• You create a tiny, harmless sensory effect that predicts what the weather will be at your location for the next 24 hours. The effect might manifest as a golden orb for clear skies, a cloud for rain, falling snowflakes for snow, and so on. This effect persists for 1 round.\n\t\t• You instantly make a flower blossom, a seed pod open, or a leaf bud bloom.\n\t\t• You create an instantaneous, harmless sensory effect, such as falling leaves, a puff of wind, the sound of a small animal, or the faint odor of skunk. The effect must fit in a 5-foot cube.\n\t\t• You instantly light or snuff out a candle, a torch, or a small campfire.", color = 0x4f094e)

			embed.add_field(name = "Level", value = "Cantrip", inline = True)

			embed.add_field(name = "School", value = "Transmutation", inline = True)

			embed.add_field(name = "Casting Time", value = "1 Action", inline = True)

			embed.add_field(name = "Range", value = "30 Feet", inline = True)

			embed.add_field(name ="Component", value = "Verbal, Somatic", inline = True)

			embed.add_field(name = "Duration", value = "Instantaneous", inline = True)

			embed.set_footer(text = "Players Handbook")
			
			await message.reply(embed = embed)




	except IndexError:

		await message.reply('Try the command again with the spell you want to see!')
