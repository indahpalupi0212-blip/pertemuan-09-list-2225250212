def rata_rata(data):
    # Memeriksa apakah list kosong
    if len(data) == 0:
        return 0

    # Menghitung rata-rata nilai
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    # Membuat list baru untuk menyimpan nilai yang lulus
    lulus = []

    # Memeriksa setiap nilai
    for n in data:
        if n >= batas:
            lulus.append(n)

    return lulus


# Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Menghitung statistik nilai
jumlah_data = len(nilai)
total_nilai = sum(nilai)
rata = rata_rata(nilai)
nilai_minimum = min(nilai)
nilai_maksimum = max(nilai)

# Menentukan nilai mahasiswa yang lulus
daftar_lulus = nilai_lulus(nilai)
jumlah_lulus = len(daftar_lulus)

# Menghitung jumlah mahasiswa yang belum lulus
jumlah_belum_lulus = jumlah_data - jumlah_lulus

# Menampilkan hasil analisis
print("=== ANALISIS NILAI MAHASISWA ===")
print("Seluruh nilai          :", nilai)
print("Banyak mahasiswa       :", jumlah_data)
print("Total nilai            :", total_nilai)
print("Rata-rata nilai        :", f"{rata:.2f}")
print("Nilai minimum          :", nilai_minimum)
print("Nilai maksimum         :", nilai_maksimum)
print("Batas kelulusan       :", 60)
print("Daftar nilai yang lulus:", daftar_lulus)
print("Jumlah mahasiswa lulus :", jumlah_lulus)
print("Jumlah belum lulus    :", jumlah_belum_lulus)