# snake water gun

# rule =>
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.

import random

print(" -----------------------------")
print("| Snake🐍 - Water💧 - Gun🔫 |")
print(" ----------------------------")

turns = int(input('How many time wanna play ?'))
listShape = ["S", "W", "G"]

userScore = 0
computerScore = 0
i = 1

while i <= turns:
    computerShape = str(random.choice(listShape))
    userShape = input("Enter Snake, Water Gun (key: S,W,G): ").upper()
    if userShape == computerShape:
        print("🟰Tie You Both Entered Same")

    elif computerShape == "W" and userShape == "S":
        print(("Computer Enter", computerShape))
        print("🐍 Snake Drink Water")
        userScore += 1

    elif computerShape == "S" and userShape == "W":
        print(("Computer Enter", computerShape))
        print("🐍 Snake Drink Water")
        computerScore += 1

    elif computerShape == "G" and userShape == "W":
        print(("Computer Enter", computerShape))
        print("💧 Gun Drowning in Water ")
        userScore += 1
    elif computerShape == "W" and userShape == "G":
        print(("Computer Enter", computerShape))
        print("💧 Gun Drowning in Water ")
        computerScore += 1

    elif computerShape == "S" and userShape == "G":
        print(("Computer Enter", computerShape))
        print("🔫 Gun Shoot the Snake")
        userScore += 1
    elif computerShape == "G" and userShape == "S":
        print(("Computer Enter", computerShape))
        print("🔫 Gun Shoot the Snake")
        computerScore += 1
    else:
        print(":(")

    print("\n\t🎯🎯🎯ScoreBoard🎯🎯🎯")
    print(f"\t You: {userScore} | Computer: {computerScore}")
    print("\t📢📢📢📢📢📢📢📢📢📢📢📢")
    print(f"Game No:[{i}]")
    print("========================================================")

    i += 1

print("\n\n🔚🔚 Game Khatam Paisa Hajam 🔚🔚")
# print("🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂🥂")
if userScore < computerScore:
    print(
        f"😑😑 Sorry You lose the game \n computer win the "
        f"game with {computerScore} score"
    )
elif userScore == computerScore:
    print(("🟰🟰 Game is Tie Play Again🟰🟰 "))
else:
    print(f"🏆🏆 You Win the Game with {userScore} score 🏆🏆")


# Fore.CYAN,
