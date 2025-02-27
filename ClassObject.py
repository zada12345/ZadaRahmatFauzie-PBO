class Mobil:
    # Konstruktor untuk menginisialisasi objek dengan atribut
    def _init_(self, merk, model, tahun, warna):
        self.merk = merk       # Atribut merk mobil
        self.model = model     # Atribut model mobil
        self.tahun = tahun     # Atribut tahun pembuatan mobil
        self.warna = warna     # Atribut warna mobil

    # Metode untuk menampilkan informasi mobil
    def tampilkan_info(self):
        return f"Mobil {self.merk} {self.model} ({self.tahun}) berwarna {self.warna}"

    # Metode untuk menyalakan mobil
    def nyalakan_mesin(self):
        return f"Mesin {self.merk} {self.model} dinyalakan."

    # Metode untuk mengendarai mobil
    def mengemudi(self):
        return f"{self.merk} {self.model} sedang dikendarai."

# Membuat objek mobil dari kelas Mobil
mobil_1 = Mobil("Toyota", "Corolla", 2020, "Merah")
mobil_2 = Mobil("Honda", "Civic", 2022, "Biru")

# Menggunakan metode dari objek mobil
print(mobil_1.tampilkan_info())   # Menampilkan informasi mobil_1
print(mobil_1.nyalakan_mesin())   # Menyalakan mesin mobil_1
print(mobil_1.mengemudi())        # Mengendarai mobil_1

print(mobil_2.tampilkan_info())   # Menampilkan informasi mobil_2
print(mobil_2.nyalakan_mesin())   # Menyalakan mesin mobil_2
print(mobil_2.mengemudi())        # Mengendarai mobil_2
