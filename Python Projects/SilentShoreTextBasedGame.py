jewel = False

def beginningScene():
	choices = ["wake up", "time travel", "escape"]
	print('"You have had quite a life Lieutenant, but it appears that you have been dancing with your own mortality."')
	print('"You have the choice to reconcile with your destiny. Choose wisely. The dominion of time now rests within your grasp."')
	userInput = ""
	while userInput not in choices:
		print('Options: 1)"wake up" Fight with your platoon. 2)"time travel" Back to before the war. 3)"escape" Try to run.')
		userInput = input()
		if userInput == "wake up":
			battleScene()
		elif userInput == "time travel":
			diplomatScene()
		elif userInput == "escape":
			print("With haste, you rise and endeavor to ascend the walls of this abyss, where shadows intertwine with skeletal echoes. Yet, an indescribable power hurls you downward onto a heap of bones.")
			print("Your hands and feet become ensnared, compelling you to confront a pivotal decision.")
			beginningScene()
		else:
			print("Please enter a valid option for the Silent Shore.")
			
def diplomatScene():
	choices = ["ac", "bs"]
	print("Abruptly awakening on a bench outside the meeting room, you scan the surroundings—Marshal Admiral Yamamoto's office looms nearby and a newspaper next to you dated 1933.")
	print("Realizing you're at Imperial HQ, heated arguments over naval strategy reverberate through the door next to you.")
	print("Drawing from wartime wisdom, you, clad in officer's fatigues, stand tall, fix your tie, and barge in.")
	print("The debate between funding battleships versus aircraft carriers escalates, and you're about to change the tide.")
	userInput = ""
	while userInput not in choices:
		print('Options: "ac" Argue that aircraft carriers should be funded, "bs" Argue that battleships should be funded')
		userInput = input()
		if userInput == "ac":
			print("You boldly steer the Japanese high command towards an air-focused navy, setting off a seismic shift in history.")
			print("Your strategic move propels Japan to triumph in the Pacific and at Midway, extending their dominion to Hawaii.")
			print("The mighty United States bows before Japan's might. Swiftly rising to Field Marshal of the Pacific, you witness the Japanese Empire reaching its pinnacle.")
			print("STATUS: YOU WON")
		elif userInput == "bs":
			print("With unwavering resolve, you persuade the Japanese high command to invest in battleships, sealing the fate of the empire against the relentless air supremacy of the United States.")
			print("In the end, victory slips away, and you stand in the shadow of defeat. You are eventually killed years later on the shores of Okinawa.")
			print("STATUS: YOU LOST")
			quit()
		else:
			print("Please enter a valid option for the Silent Shore.")

def battleScene():
	choices = ["charge", "go back"]
	global jewel
	print("You wake up to the jarring sound of violence. Bullets whiz perilously close, mingling with the anguished cries of both comrades and adversaries.")
	print("Once more, you find yourself on the shoreline, thrust back into the crucible of war.")
	print("As you scramble to regroup with your team, you find yourself at a crossroads. On the left, a wounded ally faces imminent peril as his trench is about to be overrun.")
	print("Meanwhile, directly ahead, your company prepares to launch a decisive assault on the shoreline, aiming to repel the enemy and force them back onto their awaiting vessels. Act quickly or the opportunity might be lost.")
	userInput = ""
	while userInput not in choices:
		print('Options: 1)"charge" Join your company for the assault. 2)"aid ally" Rescue your fellow soldier in need 3)"go back" Return to the fox.')
		userInput = input()
		if userInput == "aid ally":
			print("In a valiant display, you bound towards your imperiled comrade, dispatching the oncoming adversaries with unwavering resolve.")
			print("As you pivot towards him, it becomes evident that he is succumbing to his wounds.")
			print("Remaining by his side in his closing moments, he reaches for your blood-stained hand just before drawing his last breath, bestowing upon you a precious blue jewel.")
			print('"Ganbatte" he murmurs, his gaze gently fading into the embrace of mortality.')
			jewel = True
		elif userInput == "go back":
			beginningScene()
		elif userInput == "charge":
			assaultScene()
		else:
			print("Please enter a valid option for the Silent Shore.")

def assaultScene():
	actions = ["fight", "retreat"]
	global jewel
	print("With unyielding determination, you and your company storm headlong into the heart of the chaos.")
	print("Thundering forward at breakneck speed, you unleash a barrage of pinpoint-accurate gunfire on your foes, a blazing beacon of courage that electrifies your comrades.")
	print("Amidst the deafening hail of bullets, you spearhead the assault on the shoreline, embodying the valor of a true hero destined for medals.")
	print("Racing towards the last trench on the beach, your gaze locks onto the formidable remnants of the enemy's desperate resistance, the penultimate challenge before their inevitable surrender.")
	userInput = ""
	while userInput not in actions:
		print('Options: "retreat" or "fight"')
		userInput = input()
		if userInput == "fight":
			if jewel:
				print("In an epic display of unwavering bravery, you wage a relentless battle to drive your adversaries from the island, and triumph is yours.")
				print("The fierce combat on the shores of Okinawa grinds to a dramatic halt on the 7th of June, a ceasefire born of mutual respect for the fallen and the wounded.")
				print("Soldier, you have successfully reconciled with your fate, embracing your destiny. Well done!")
				print("STATUS: YOU WON")
			else:
				print("In a heart-stopping battle, you fight with unyielding determination, pushing yourself to the very brink.")
				print("Yet, in a twist of fate, a brutal confrontation unfolds, and you find yourself on the losing end, a sharp bayonet thrust plunging into your chest.")
				print("The relentless struggle showcases your indomitable spirit, even in the face of a harrowing defeat.")
				print("STATUS: YOU LOST")
			quit()
		elif userInput == "retreat":
			battleScene()
		else:
			print("Please enter a valid option for the Silent Shore.")
		

if __name__ == "__main__":
		while True:
			print("Welcome to Silent Shore.")
			print("It is the 6th of June, 1945.")
			print("You slowly awaken, only to hear the rhytmic lull of distant waves and the faint cadence of exchanged gunfire.")
			print("As you lift your gaze, you see that you're still in Okinawa.")
			print("The eerily quiet predawn atmosphere is shrouded in mist, concealing the expanse of the beach.")
			print("As you gather your scattered equipment, your eyes meet with a white fox sitting at the edge of the ridge.")
			print("It's gaze is fixed directly upon you.")
			print('"A kitsune..." you whisper')
			print("You find your dogtag covered in sand. It states your name: ")
			name = input()
			print("Lieutenant " +name+ ", 89th Infantry Division, 8874976.")
			print("You proceed to cautiously navigate along the ridge, heading towards the fox.")
			print("As you approach it, the fox swiftly dashes into an abandoned tunnel embedded within the ridge.")
			print("You hastily pursue it, and suddenly, you descend through the tunnel's floor into a dark room.")
			print("You reach for your lighter, casting a subtle glow across the dim room.")
			print("In the distance, you discern red eyes peering through the darkness, piercing into your soul.")
			print("As it draws near, fangs bared, The fox starts to speak to you.")
			print("It's ethereal voice seemed intimately near, as if emanating from within your own mind, intertwining seamlessly with your thoughts.")
			beginningScene()

