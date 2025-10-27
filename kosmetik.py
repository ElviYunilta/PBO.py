class Kosmetik(object):
    nama = None

    def __init__(self, nama):
        self.nama = nama

    def pakai(self):
        print('{} sedang digunakan'.format(self.nama))


class KosmetikWanita(Kosmetik):
    jenis = None
    warna = None

    def __init__(self, nama, jenis):
        super().__init__(nama)  # gunakan super() untuk memanggil konstruktor parent
        self.jenis = jenis

    def set_warna(self, warna):
        self.warna = warna


# Contoh penggunaan
lipstick = KosmetikWanita("Lipstick", "Makeup Bibir")
lipstick.set_warna("Merah")
lipstick.pakai()
print("Jenis:", lipstick.jenis)
print("Warna:", lipstick.warna)
