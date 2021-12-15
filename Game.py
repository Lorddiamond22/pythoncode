print("Membuat Game Sederhana Dengan Python")
print(37*"=")
print("Daftar Game")
print("1. Tebak Angka")
print("2. Suit")
print("3. Tic Tac Toe")

game = input('Pilih Angka Berapa: ')

if(game == '1'):   
    import random
    print('Game Tebak Angka')
    attempts_list = []
    def show_score():
        if len(attempts_list) <= 0:
            print("Saat ini belum ada skor tertinggi, kesempatan Anda untuk mengambilnya!")
        else:
            print("Skor tertinggi saat ini adalah {} percobaan".format(min(attempts_list)))
    def start_game():
        random_number = int(random.randint(1, 100))
        print("Halo petualang! Selamat datang pada permainan tebak-tebakan angka!")
        player_name = input("Siapa nama Anda? ")
        wanna_play = input("Hi, {}, apakah Anda ingin bermain tebak angka? (ya/tidak) ".format(player_name))
        
        attempts = 0
        show_score()
        while wanna_play.lower() == "ya":
            try:
                guess = input("Pilih angka antara 1 dan 100: ")
                if int(guess) < 1 or int(guess) > 100:
                    raise ValueError("Silahkan tebak angka di antara nya")
                if int(guess) == random_number:
                    print("Selamat! Anda benar!")
                    attempts += 1
                    attempts_list.append(attempts)
                    print("Anda melakukannya dengan {} percobaan".format(attempts))
                    play_again = input("Apakah Anda ingin bermain lagi? (Ya/Tidak) ")
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1, 100))
                    if play_again.lower() == "tidak":
                        print("Terima kasih, sampai jumpa kembali!")
                        break
                elif int(guess) > random_number:
                    print("Angkanya terlalu besar")
                    attempts += 1
                elif int(guess) < random_number:
                    print("Angkanya terlalu kecil")
                    attempts += 1
            except ValueError as err:
                print("Oh tidak!, ini nilai yang salah. Silahkan mencoba lagi...")
                print("({})".format(err))
        else:
            print("Selamat, telah bermain game ini!")
    if __name__ == '__main__':
        start_game()

elif(game == '2'):
    def game():
        import random
        print('Game Gunting Batu Kertas')
        print("1. ROCK")
        print("2. PAPER")
        print("3. SCISSORS")


        player_choose = int(input("Pilih Angka Berapa: "))

        com_choice = [1, 2, 3]

        print("\nComputer Choice")
        com_choose = (random.choice(com_choice))

        print(": ", com_choose, "\n")


        if player_choose == 1 and com_choose == 1:
            print("\t\tBatu VS Batu\n")
            print("\t\tDRAW !")
        elif player_choose == 1 and com_choose == 2:
            print("\t\tBatu VS Kertas\n")
            print("\t\tKamu Kalah !")
        elif player_choose == 1 and com_choose == 3:
            print("\t\tBatu VS Gunting\n")
            print("\t\tKamu Menang !")

        elif player_choose == 2 and com_choose == 1:
            print("\t\tKertas VS Batu\n")
            print("\t\tKamu Menang !")
        elif player_choose == 2 and com_choose == 2:
            print("\t\tKertas VS Kertas\n")
            print("\t\tDRAW !")
        elif player_choose == 2 and com_choose == 3:
            print("\t\tKertas VS Gunting\n")
            print("\t\tKamu Kalah !")

        elif player_choose == 3 and com_choose == 1:
            print("\t\tGunting VS Batu\n")
            print("\t\tKamu Kalah !")
        elif player_choose == 3 and com_choose == 2:
            print("\t\tGunting VS Kertas\n")
            print("\t\tKamu Menang !")
        elif player_choose == 3 and com_choose == 3:
            print("\t\tGunting VS Gunting\n")
            print("\t\tDRAW !")

            

        print(50*"=")
    game()
    game()
    game()


elif(game == '3'):
    import random
    import sys
    print('Game Tic Tac Toe')
    board=[i for i in range(0,9)]
    player, computer = '',''
    # Pojok, tengah dan lokasi lainnya, berturut-turut
    moves=((1,7,3,9),(5,),(2,4,6,8))
    # Kombinasi pemenang
    winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    # Tabel
    tab=range(1,10)
    def print_board():
        x=1
        for i in board:
            end = ' | '
            if x%3 == 0:
                end = ' \n'
                if i != 1: end+='---------\n';
            char=' '
            if i in ('X','O'): char=i;
            x+=1
            print(char,end=end)
    def select_char():
        chars=('X','O')
        if random.randint(0,1) == 0:
            return chars[::-1]
        return chars
    def can_move(brd, player, move):
        if move in tab and brd[move-1] == move-1:
            return True
        return False
    def can_win(brd, player, move):
        places=[]
        x=0
        for i in brd:
            if i == player: places.append(x);
            x+=1
        win=True
        for tup in winners:
            win=True
            for ix in tup:
                if brd[ix] != player:
                    win=False
                    break
            if win == True:
                break
        return win
    def make_move(brd, player, move, undo=False):
        if can_move(brd, player, move):
            brd[move-1] = player
            win=can_win(brd, player, move)
            if undo:
                brd[move-1] = move-1
            return (True, win)
        return (False, False)
    
    # Komputer AI menggunakan function di bawah ini
    def computer_move():
        move=-1
        # Jika saya menang, yang lain tidak dihiraukan.
        for i in range(1,10):
            if make_move(board, computer, i, True)[1]:
                move=i
                break
        if move == -1:
        # Jika player menang, lakukan penghadangan.
            for i in range(1,10):
                if make_move(board, player, i, True)[1]:
                    move=i
                    break
        if move == -1:
            # Mencoba mengambil posisi yang di inginkan.
            for tup in moves:
                for mv in tup:
                    if move == -1 and can_move(board, computer, mv):
                        move=mv
                        break
        return make_move(board, computer, move)
    def space_exist():
        return board.count('X') + board.count('O') != 9
    player, computer = select_char()
    print('Player adalah [%s] dan komputer adalah [%s]' % (player, computer))
    result='%%% Seri ! %%%'
    
    
    while space_exist():
        print_board()
        print('#Silahkan memulai duluan ! [1-9] : ', end='')
        move = int(input())
        moved, won = make_move(board, player, move)
        if not moved:
            print(' >> Input tidak valid ! Coba lagi !')
            continue
        
        if won:
            result='*** Selamat ! Anda memenangkannya ! ***'
            break
        elif computer_move()[1]:
            result='=== Maaf Anda kalah! Silahkan mencoba lagi di lain kesempatan ! =='
            break;
    print_board()
    print(result)

