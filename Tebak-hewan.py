def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 5:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 5:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Hewan yang suka kebersihan? ")
check_guess(guess1, "Gajah")
guess2 = input("Kepiting kalo kegunting jadi? ")
check_guess(guess2, "Kepotong")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
guess4 = input("Which is the larget animal? ")
check_guess(guess4, "Blue Whale")
guess5 = input("Which is the larget animal? ")
check_guess(guess5, "Blue Whale")
print("Your Score is "+ str(score))