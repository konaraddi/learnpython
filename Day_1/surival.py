# By using "input" instead of "print", the user needs to hit ENTER to continue
# If we were to use "print" for all the prompts, the consecutive prompts would appear instantly

input("You're stranded on the shore of an island.")
input("You're very hungry.")
input("There's some cyanide in your back pocket.")

action= input("Do you consume the cyanide? (YES/NO)")

if action == "YES":
	input("Cyanide isn't good for you, so you died.")
	input("Coward. Taking the easy way out....")
elif action == "NO":
	input("Yes! That's the spirit!")
	input("It's too early in the game to give up.")
	input("You notice there's a crab and injured seagull nearby.")

	action=input("Do you eat the CRAB or the SEAGULL?")
	if action == "CRAB":
		input("You ate the crab raw? Boi, you died.")
	elif action == "SEAGULL":
		input("You are the seagull raw? Gross.")
		input("You just vomitted. At least you're alive.")
	else:
		print("Failure to follow directions.")
		print("You DIED.")

else:
	print("Failure to follow the directions led to this fate:")
	print("You DIED.")
