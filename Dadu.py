import random

def roll_dice():
    dice_number = random.randint(1, 6)
    return dice_number

print("===== Welcome to Dadu Simulator =====")
print("===== Script Ini Bisa Digunakan Jika Dadu Kamu Hilang =====")
while 1:
    choice = input("Kamu Ingin Mengkocok Dadu? (y/n)")
    if 'y' in choice.lower():
        print("Mengkocok Dadu...")
        number = roll_dice()
        print("Yaa Kamu Mengapatkan Angka:", number)
    elif 'n' in choice.lower():
        print('Keluar...')
        break
    else:
        print("Invalid input...please try again")
        