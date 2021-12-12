while True:
    user = input("Username: ")
    import getpass

    sandi = getpass.getpass()

    if sandi == '123' and user == 'abc':
        print("Anda Telah Login")
        while True:
            print('Program Jadwal Pelajaran')
            hari = input('Masukkan Hari: ')

            if(hari == 'senin'):
                print('Jadwal Pelajaran Hari Senin')
                print('1. PKWU')
                print('2. Ekonomi')
                print('3. Bahasa Indonesia')
                print('4. Geografi')

            elif(hari == 'selasa'):
                print('Jadwal Pelajaran Hari Selasa')
                print('1. Matematika Wajib')
                print('2. BK')
                print('3. Sejarah Indonesia')
                print('4. PJOK')

            elif(hari == 'rabu'):
                print('Jadwal Pelajaran Hari Rabu')
                print('1. English Conversation')
                print('2. Fisika')
                print('3. TIK')
                print('4. PPKN')

            elif(hari == 'kamis'):
                print('Jadwal Pelajaran Hari Kamis')
                print('1. Agama Islam')
                print('2. Seni Budaya')
                print('3. Biologi')
                print('4. Matematika Minat')

            elif(hari == 'jumat'):
                print("Jadwal Pelajaran Hari Jum'at")
                print('1. Bahasa Inggris')
                print('2.Bahasa Jepang')
                print('3. Kimia')

            elif(hari == 'sabtu'):
                print('Libur gann')

            elif(hari == 'minggu'):
                print('Libur gann')

            elif(hari == 'close'):
                break

            else:
                print("Maaf Perintah Anda Salah")
    else:
        print("Username atau Password Anda Salah")