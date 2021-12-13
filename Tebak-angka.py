# to import random module
import random
# to create a range of random numbers between 1-10
n = random.randrange(1,100)
# to take a user input to enter a number
print('Game Tebak Angka')
guess = int(input("Masukkan Angka: "))
while n!= guess: # means if n is not equal to the input guess
    # if guess is smaller than n
    if guess < n:
        print("Terlalu Kecil!")
        # to again ask for input
        guess = int(input("Masukkan Angka Lagi: "))
    # if guess is greater than n
    elif guess > n:
        print("Terlalu Besar!")
        # to again ask for the user input
        guess = int(input("Masukkan Angka Lagi: "))
    # if guess gets equals to n terminate the while loop
    else:
        break
print("Ya Kamu Berhasil!!")