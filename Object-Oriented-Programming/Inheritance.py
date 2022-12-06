class awal:
    def __init__(self):
        self.kelas = "10 PPLG 2"
        self.nama = "Ababil"
        self.umur = "16"

    def namasaya(self):
        print(f"Nama Saya Adalah {self.nama}")

    def kelassaya(self):
        print(f"Saya kelas {self.kelas}")

    def umursaya(self):
        print(f"Dan Umur Saya {self.umur} Tahun")


class keluarga(awal):

    def __init__(self):
        self.anakce = "1"

    def jumlah(self, anakce, nama):
        print(f"Saya {self.nama} Anak Ke {self.anakce}")


kel = keluarga()
kel.jumlah()

