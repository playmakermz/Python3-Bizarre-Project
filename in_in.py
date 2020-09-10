from data import data
class store():
    
    data_a = int(data['tabungan'])

    def __init__(self, input_1, input_2):
        self.name = input_1
        self.password = input_2
    
    def To_Myself(self):
        
        tambah = int(input('masukan uang :'))
        
#        tambah = int(tambah)
        if type(tambah) == int:
            pertanyaan = input('''
            'y' untuk simpan, 'n' untuk tidak
            :''')

            if pertanyaan == 'y' or pertanyaan == 'Y':
                store.data_a += tambah
                print('uang anda saat ini adalah {}'.format(store.data_a))

            else:
                print('di batalkan')

        else:
            print('uang harus int')
    
    def To_Other(self):

        tambah = int(input('masukan uang :'))

     #   tambah = int(tambah)
        if type(tambah) == int:
            pertanyaan = input('''
            'y' untuk kirim, 'n' untuk tidak
            ''')

            if pertanyaan == 'y' or pertanyaan == 'Y':
                print('{} telah di kirim'.format(tambah))


        else:
            print('uang harus int')

#print(store.data_a)
#if __name__ == '__main__':
#    masukan = store('budi','123')
#    while True:
#        masukan.To_Myself()



