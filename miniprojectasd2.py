class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Perabot:
    def __init__(self, nomor, nama, harga, stok, kualitas):
        self.nomor = nomor
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kualitas = kualitas

class CRUD:
    def __init__(self):
        self.head = None

    def tambah_barang_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_barang_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def tambah_barang_antara(self, prev_data, data):
        new_node = Node(data)
        if prev_data is None:
            print("Data sebelumnya tidak ditemukan.")
            return
        new_node.next = prev_data.next
        prev_data.next = new_node

    def hapus_barang(self, nomor):
        temp = self.head
        if temp is not None:
            if temp.data['nomor'] == nomor:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data['nomor'] == nomor:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print("Barang tidak ditemukan.")
            return
        prev.next = temp.next
        temp = None

    def lihat_barang(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def update_stok(self, nomor, stok):
        temp = self.head
        while temp:
            if temp.data['nomor'] == nomor:
                temp.data['stok'] = stok
                return
            temp = temp.next
        print("Barang tidak ditemukan.")

def main_menu():
    crud_instance = CRUD()
    while True:
        print("==== Menu ====")
        print("1. Tambah barang di awal")
        print("2. Tambah barang di akhir")
        print("3. Tambah barang di antara")
        print("4. Lihat barang")
        print("5. Hapus barang")
        print("6. Update stok")
        print("7. Keluar")

        menu = int(input("Pilih 1/2/3/4/5/6/7: "))

        if menu == 1:
            tambah_barang_awal_menu(crud_instance)
        elif menu == 2:
            tambah_barang_akhir_menu(crud_instance)
        elif menu == 3:
            tambah_barang_antara_menu(crud_instance)
        elif menu == 4:
            lihat_barang_menu(crud_instance)
        elif menu == 5:
            hapus_barang_menu(crud_instance)
        elif menu == 6:
            update_stok_menu(crud_instance)
        elif menu == 7:
            print("Terima kasih!")
            break

def tambah_barang_awal_menu(crud_instance):
    nomor = int(input("Nomor: "))
    nama = input("Nama: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    kualitas = input("Kualitas: ")
    data = {"nomor": nomor, "nama": nama, "harga": harga, "stok": stok, "kualitas": kualitas}
    crud_instance.tambah_barang_awal(data)
    print("Barang telah ditambahkan di awal.")

def tambah_barang_akhir_menu(crud_instance):
    nomor = int(input("Nomor: "))
    nama = input("Nama: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    kualitas = input("Kualitas: ")
    data = {"nomor": nomor, "nama": nama, "harga": harga, "stok": stok, "kualitas": kualitas}
    crud_instance.tambah_barang_akhir(data)
    print("Barang telah ditambahkan di akhir.")

def tambah_barang_antara_menu(crud_instance):
    nomor_sebelumnya = int(input("Nomor barang sebelumnya: "))
    nomor = int(input("Nomor: "))
    nama = input("Nama: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    kualitas = input("Kualitas: ")
    data = {"nomor": nomor, "nama": nama, "harga": harga, "stok": stok, "kualitas": kualitas}
    temp = crud_instance.head
    while temp:
        if temp.data['nomor'] == nomor_sebelumnya:
            crud_instance.tambah_barang_antara(temp, data)
            print("Barang telah ditambahkan di antara.")
            return
        temp = temp.next
    print("Nomor barang sebelumnya tidak ditemukan.")

def lihat_barang_menu(crud_instance):
    print("Daftar Barang:")
    crud_instance.lihat_barang()

def hapus_barang_menu(crud_instance):
    nomor = int(input("Nomor barang yang akan dihapus: "))
    crud_instance.hapus_barang(nomor)
    print("Barang telah dihapus.")

def update_stok_menu(crud_instance):
    nomor = int(input("Nomor barang yang akan diupdate stok: "))
    stok_baru = int(input("Stok baru: "))
    crud_instance.update_stok(nomor, stok_baru)
    print("Stok barang telah diupdate.")

if __name__ == "__main__":
    main_menu()
