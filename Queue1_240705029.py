class Queue:
    def __init__(self):
        self.qlist = list()

    def isEmpty(self):
        return len(self.qlist) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        if self.isEmpty():
            print('Queue kosong. Tidak ada data yang dapat di-dequeue.')
            return
        else:
            return self.qlist.pop(0)

    def display(self):
        if self.isEmpty():
            print('Queue kosong. Tidak ada data yang dapat ditampilkan.')
        else:
            for item in self.qlist:
                print(item, end=' ')
            print() # Menambahkan newline setelah selesai display

    def DeleteAll(self):
        while not self.isEmpty():
            self.dequeue()

#Create Queue
myQueue = Queue()
cek = True

while cek:
    print()
    print('-----Masukan Pilihan anda-----')
    print(' 1. Tambah Elemen pada Queue')
    print(' 2. Tampil Elemen dalam Queue')
    print(' 3. Hapus Elemen dalam Queue')
    print(' 4. Hapus Seluruh data dalam Queue')
    print(' 0. Keluar')
    print()

    pil = int(input('Masukan Pilihan anda: '))

    if pil == 1:
        jum = int(input('Masukan jumlah data yang ingin diinputkan: '))
        if jum > 0:
            i = 1
            while i <= jum:
                data = input('Masukan data yang ingin diinput: ')
                myQueue.enqueue(data)
                i += 1
        else:
            print('Jumlah data minimal 1 !!!')

    elif pil == 2:
        print('Isi Queue: ')
        myQueue.display()

    elif pil == 3:
        myQueue.dequeue()
        print('Data telah dihapus') # Di gambar 7.jpg, baris ini ada setelah myQueue.dequeue()

    elif pil == 4:
        myQueue.DeleteAll()
        print('Seluruh Data telah dihapus')

    elif pil == 0:
        print('Bye troopers... \n')
        cek = False
        break

    else:
        print('Pilihan tidak ada')