import time
print("===== Alarm Dengan Python =====")

def set_countdown():
    seconds = int(input("Berapa Detik Alarm Akan Berjalan: "))
    print('Alarm Dimulai...')
    temp = seconds
    while temp != 0:
        if temp != seconds:
            print('\b'*len(str(temp)), end='')
        time.sleep(1)
        temp -= 1
        print(temp, end='')
    print("\nAlarm Berhenti...\n")

while 1:
    choice = input("Kamu Ingin Menggunakan Alarm (y/n): ")
    if 'y' in choice.lower():
        set_countdown()
    elif 'n' in choice.lower():
        print('Keluar...')
        break
    else:
        print('Invalid input...please try again')