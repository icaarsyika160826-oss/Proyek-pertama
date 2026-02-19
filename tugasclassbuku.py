class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status = "tersedia"

    def tampilkan_info(self):
        print("Judul:", self.judul)
        print("Penulis:", self.penulis)
        print("Tahun Terbit:", self.tahun_terbit)
        print("Status:", self.status)
        print()

    def ubah_status(self, status_baru):
        self.status = status_baru


class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.daftar_buku = []

    def pinjam_buku(self, buku):
        if buku.status == "tersedia":
            buku.ubah_status("dipinjam")
            self.daftar_buku.append(buku)
            print(f"{self.nama} berhasil meminjam buku {buku.judul}")
        else:
            print("Buku sedang dipinjam")

    def kembalikan_buku(self, buku):
        if buku in self.daftar_buku:
            buku.ubah_status("tersedia")
            self.daftar_buku.remove(buku)
            print(f"{self.nama} mengembalikan buku {buku.judul}")
        else:
            print("Buku tidak ada dalam daftar pinjaman")




buku1 = Buku("Gunung", "Icha", 2020)
anggota1 = Anggota("Arsy", 12345)

anggota1.pinjam_buku(buku1)
buku1.tampilkan_info()

anggota1.kembalikan_buku(buku1)
buku1.tampilkan_info()
