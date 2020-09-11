from customer import Customer
import random
import datetime

nasabah_atm = Customer(id)
trial = 0
while True:
    id = int(input('masukan pin :'))


    while (id != int(nasabah_atm.ambilPin()) and trial <= 3):
        id = int(input('masukan pin lagi :'))
        trial += 1

        if trial >= 3:
            print('anda telah salah 3 kali')
            break
        
    while True:
        print('''
selamat datang 
1) cek saldo
2) debet
3) simpan
4) ganti pin
5) Keluar

            ''')

        select_input = int(input())

        if select_input == 1:
            print(nasabah_atm.ambilBalance())
        elif select_input == 2:
            inputn = float(input('masukan nominal saldo :'))
            pertanyaan = input('konfirmasi apakah anda memasukan debet senilai {} :'.format(inputn))
            if pertanyaan == 'y':
                print('saldo awal anda {}'.format(nasabah_atm.ambilBalance()))
            else:
                break

            if inputn < nasabah_atm.ambilBalance():
                nasabah_atm.ambiluang(inputn)
                print('transalsi berhasi')
                print('tersisa {}'.format(nasabah_atm.ambilBalance()))
            else:
                print('uang anda tidak mencukupi')
                break


        elif select_input == 3:
            inputs = input('masukan nominal untuk di simpan :')
            pertanyaan = input('(y)/(n) apakah di lanjutkan atau tidak :')

            if pertanyaan == 'y':
                nasabah_atm.simpanuang(int(inputs))
                print('saldo anda saat ini {}'.format(nasabah_atm.ambilBalance()))

            else:
                break

        elif select_input == 4:
            verif = int(input('masukan pin lama :'))

            while verif != int(nasabah_atm.ambilPin()):
                print('maaf pin anda salah')
                break

            inputpin = int(input('masukan pin baru :'))
            print('pin baru anda berhasil')

            verifpin = int(input('coba masukan pin baru :'))

            if inputpin == verifpin:
                print('pin baru anda berhasil')
            else:
                print('maaf, pin anda salah')

        elif select_input == 5:
            print('resi tercetak otomatis')
            print('No, Resi {}'.format(random.randint(100000, 1000000)))
            print('Tanggal : {}'.format(datetime.datetime.now()))
            print('saldo terakhi : {}'.format(nasabah_atm.ambilBalance()))
            print('terimakasih')
            exit()

                    

        else:
            print('maaf tidak menu selain di atas')

