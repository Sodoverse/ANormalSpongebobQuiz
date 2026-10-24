import webbrowser

print("Welecome to the Spongebob Quiz!")

score = 0

answer = input("1. Where does Spongebob work?: ")

if answer.lower() == "krusty krab":
    print("Correct!")
    score = score + 1
    print(f"Your score = {score}")
else:
    print("ARE YOU DUMB ASS FUCK!? HE WORKS IN THE KRUSTY CRAB. NO POINTS, BITCH!")
    print(f"Your score = {score}")
    
answer = input("2. How big is spongebob's dick?: ")

if answer.lower() == "2 inches":
    print("I don't know how you knew that. But, hey! It's correct!")
    score = score + 1
    print(f"Your score = {score}")
else:
    print("It's fine, bro. I didn't know that either. Still gotta take from you though, bitch ass nigga.")
    print(f"Your score = {score}")

answer = input("3. Who is Spongebob's best friend?: ")
    
if answer.lower() == "patrick star":
    print("Correct!")
    score = score + 1
    print(f"Your score = {score}")
else:
    print("NIGGA, IT'S PATRICK! HOW TF DON'T YOU KNOW ABOUT PATRICK!? BITCH, I'M TAKING NEGATIVE POINTS!")
    score = score - 100
    print(f"Your score = {score}")
          
answer = input("4. What kind of animal is Gary!?")

if answer.lower() == "snail":
    print("Correct! You win!")
    score = score + 1
    print(f"Your score = {score}")
else:
    print("Yo, nigga. Get the fuck out of my game. In fact, go use this shit, right now.")
    webbrowser.open("https://sodoverse.github.io/Pornhub-Roulette-/")