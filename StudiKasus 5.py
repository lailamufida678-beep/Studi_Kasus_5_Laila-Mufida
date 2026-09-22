daftar_kendaraan = {
    1: "Mobil",
    2: "Motor"
}

def hitung_biaya_parkir(jenis_kendaraan, durasi):
    if jenis_kendaraan == "Mobil":
        tarif = 5000
    elif jenis_kendaraan == "Motor":
        tarif = 3000
    else:
        tarif = 0

    return tarif * durasi

jenis = input("Masukkan Jenis Kendaraan Anda(Mobil/Motor): ")
jam_masuk = int(input("Jam Masuk: "))
jam_keluar = int(input("Jam Keluar: "))

lama_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir(jenis, lama_parkir)

print("Data Akhir")
print("Kendaraan: ", jenis)
print("Jam Masuk: ", jam_masuk)
print("Jam Keluar: ", jam_keluar)
print("Lama Parkir: ", lama_parkir, "jam")
print("Total Biaya: Rp", total_biaya)