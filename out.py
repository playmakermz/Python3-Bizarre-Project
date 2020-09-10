from data import data

#print(store.data_a)

class transfer():

    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def Kirim(self):
        
        uang = int(input('masukan uang untuk di ambil:'))
        if data['tabungan'] >= uang:
            data['tabungan'] -= uang
            print('uang telah dikirim, uang tersisa {}'.format(data['tabungan']))
        else:
            print('uang anda tidak mencukupi')


#if __name__ == '__main__':
 #   print(store.data_a)
