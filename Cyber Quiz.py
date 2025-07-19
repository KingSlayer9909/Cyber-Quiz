score=0
print("Welcome to the Cybersecurity Quiz!")

#Question 1
print("1. What does VPN stand for?")
print("a) Very Private Network\nb)Virtual Private Network\nc)Virtual Public Network\nd)Virtual Public Node")
answer1 =input(">").lower()


if answer1 == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is b) Virtual Private Network.\n")

#Question 2
print("2. What is phishing?")
print("a)Email scam\nb)Firewall breach\nc)Encryption method")
answer = input("> ").lower()

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! the correct answer is a) Email scam.\n")

#Question 3
print("3. What's a strong password?")
print("a)123456\nb) qwerty\nc) !Wolv3r1ne@2025")
answer =input("> ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is c) !Wolv3er1ne@2025.\n")

# Final Score
print(f"Your final score: {score}/3")

if score == 3:
    print ("You're a cyber pro")
elif score == 2:
    print("Nice job! You're learning.")
else:
    print("Keep studying!")