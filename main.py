import random
normal = ["Yes, definitely", "No way", "Ask again later", "Without a doubt", "My sources say no", "Concentrate and ask again", "Signs point to yes", "Very doubtful"]
funny = ["Skill issue", "100% yes", "Not in a million years", "Maybe... if you're lucky", "Why are you asking me?", "Absolutely not", "Bro, what?", "Even I don't know"]
anserthingy = input("do you want to use the funny or normal ansers?(funny/normal)")
if anserthingy == "funny":
    anserthingy = funny
else:
    anserthingy = normal
idk = 0
idk2 = (len(anserthingy) - 1)
while True:
    idk3 = input("enter a question: ")
    idk = random.randint(0, idk2)
    print(anserthingy[idk])
    exitquestion = input("do you want to exit(y/n)? ")
    if exitquestion == "y":
        print("exiting...")
        break