print("Welcome to my game ")
playing = input(" Do you want to play with me? ")

if playing.lower() != "yes": 
    quit()
print("Okay, Let's go " )
score = 0

answer = input("What is the lowest level of coding language? ").lower()
if answer == "assembly":
    print('correct')
    score +=1
else: 
    print('Incorrect!')
    
answer = input("Asking users to reveal sensitive or personal information over the phone is referred to as .... ? ").lower()
if answer == "social engineering":
    print('correct')
    score += 1
else: 
    print('Incorrect!')
    
answer = input("Wi-Fi networks that are ... are unsecure and should not be used. ").lower()
if answer == "open":
    print('correct')
    score += 1
else: 
    print('Incorrect!')


answer = input("Which TCP/IP service resolves host names to IP addresses? ").lower()
if answer == "dns":
    print('correct')
    score += 1
else: 
    print('Incorrect!')


if score < 4:
    print("Your score is " + str(score) + " noob")
else:
    print("Your score is " + str(score) + " PRO")
        
    
