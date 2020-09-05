class hitung():
    # ini untuk class pertama
    def __init__(self, nilai_x,nilai_y):
        self.x = nilai_x
        self.y = nilai_y

class FPB(hitung): # inheritance

    def hit(self):
        dataX = [] # list untuk x, y
        dataY = []
        x = int(self.x)
        y = int(self.y)
        print(x, y)
        for xi in range(x): # loop mengambil number
            xi += 1
            xi = x/xi
            if xi == int(xi):
                dataX.append(int(xi))

        for yi in range(y):
            yi += 1
            yi = y/yi
            if yi == int(yi):
                dataY.append(int(yi))

        dataX.extend(dataY) # gabungkan list x dan y
        
        
        _size = len(dataX)
        repeat = []

        for item in range(_size): # mencocokan
            item_g = item + 1
            for item_2 in range(item_g, _size):
                if dataX[item] == dataX[item_2] and dataX[item] not in repeat:
                    repeat.append(dataX[item])

        return repeat
        

if __name__ == '__main__': # perintah di jalankan
    # ini hanyalah contoh
    inX = int(input('msukan X:'))
    inY = int(input('masukan Y:'))
    coba = FPB(inX, inY)
    print('hasil FPB dari {} dan {}'.format(inX, inY))
    print('Hasil : {}'.format(max(coba.hit())))
