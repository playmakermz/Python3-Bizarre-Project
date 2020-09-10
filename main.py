from in_in import store
from out import transfer
from data import data

if __name__ == '__main__':

    while True:
        username = input('username :')
        password_i = input('password :')
    
        hasil = '{} and {}'.format(username, password_i)
        per = '{} and {}'.format(data['name'], data['password'])
        if hasil == per:
            print('selamat datang {}'.format(username))
        
            pilihan = input('''
(1). store tunai
(2). tarik tunai

:''')
            if pilihan == '1':
                print(''' 
 store Tunai

(1) untuk akun ini
(2) untuk akun lain
:''')
                pilihan_2 = input(':')
                if pilihan_2 == '1':
                    akun_saya = store(data['name'], data['password'])
                    akun_saya.To_Myself()

                elif pilihan_2 == '2':
                    akun_saya = store(data['name'], data['password'])
                    akun_saya.To_Other()
                else:
                    print('eror')

            elif pilihan == '2':
                print('''
Tarik tunai
''')
                akun_saya = transfer(data['name'], data['password'])
                akun_saya.Kirim()

            else:
                print('eror main')

            akhir = input('berhenti ? (y)/(n)')
            if akhir == 'y' or akhir == 'Y':
                break
