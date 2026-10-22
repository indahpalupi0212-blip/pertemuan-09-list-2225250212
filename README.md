# Pertemuan 9 - List dan Pengolahan Data Numerik

**Nama:** Indah Palupi Kusumaningrum

**NIM:** 2225250212

**Kelas:** 3F

## 1. Tujuan

Mempelajari penggunaan list pada Python untuk menyimpan dan mengolah kumpulan data numerik. Materi ini juga melatih penggunaan indeks, manipulasi list, perulangan, fungsi, serta perhitungan statistik sederhana.

## 2. Materi yang Dipelajari

- Membuat list dan menyimpan beberapa nilai dalam satu variabel.
- Mengakses elemen list menggunakan indeks positif dan negatif.
- Mengambil sebagian elemen menggunakan slicing.
- Menambah, mengubah, dan menghapus elemen list.
- Menelusuri data menggunakan perulangan `for`.
- Menghitung jumlah data, total, rata-rata, nilai minimum, dan maksimum.
- Menggunakan fungsi untuk mengolah data.
- Menentukan kelulusan mahasiswa berdasarkan batas nilai 60.

## 3. Struktur Program

```text
pertemuan-09-list-NIM/
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
├── praktik/
│   └── analisis_nilai_mahasiswa.py
├── .gitignore
└── README.md
```

## 4. Penjelasan Latihan

### A. Membuat List
Mempelajari cara membuat list untuk menyimpan beberapa data dalam satu variabel.

### B. Indeks dan Slicing
Mempelajari cara mengakses elemen berdasarkan indeks dan mengambil sebagian elemen list.

### C. Manipulasi List
Mempelajari cara menambah, mengubah, dan menghapus elemen pada list.

### D. Agregasi Nilai
Menggunakan fungsi Python seperti `sum()`, `len()`, `min()`, dan `max()` untuk mengolah data numerik.

### E. Filter Kelulusan
Menyaring nilai mahasiswa berdasarkan batas kelulusan 60.

### F. Fungsi Statistik
Mempelajari cara membuat fungsi untuk mengolah kumpulan data numerik.

## 5. Praktik Analisis Nilai Mahasiswa

File praktik yang digunakan adalah:

`praktik/analisis_nilai_mahasiswa.py`

Program ini mengolah 10 nilai mahasiswa dan menampilkan ringkasan statistik serta informasi kelulusan.

Fitur program:
- Menampilkan seluruh nilai mahasiswa.
- Menghitung banyak data dan total nilai.
- Menghitung rata-rata nilai.
- Menentukan nilai minimum dan maksimum.
- Menentukan batas kelulusan sebesar 60.
- Menghitung jumlah mahasiswa yang lulus dan belum lulus.
- Membuat list baru yang berisi nilai mahasiswa yang lulus.
- Menggunakan fungsi `rata_rata()` dan `nilai_lulus()`.

## 6. Cara Menjalankan Program

Pastikan Python sudah terpasang dan file telah dibuka melalui VS Code.

Jalankan latihan dengan perintah:

```bash
python latihan/01_buat_list.py
```

Untuk menjalankan praktik analisis nilai mahasiswa:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

Jika perintah `python` tidak berfungsi, coba gunakan `python3`.

## 7. Pengujian Program

Pengujian dilakukan untuk memastikan perhitungan statistik dan penentuan kelulusan berjalan dengan benar.

| Data Nilai | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| `[60, 70, 80]` | Rata-rata | 70.00 |
| `[60, 70, 80]` | Minimum dan maksimum | 60 dan 80 |
| `[60, 70, 80]` | Jumlah mahasiswa lulus | 3 |
| `[59, 60, 61]` | Kelulusan dengan batas 60 | 2 lulus |
| `[]` | Fungsi rata-rata pada list kosong | Tidak menyebabkan error pembagian dengan nol |

**Catatan:** Hasil aktual pengujian dicatat setelah program dijalankan.

## 8. Kesimpulan

Melalui Pertemuan 9, saya mempelajari penggunaan list untuk menyimpan dan mengolah kumpulan data numerik menggunakan Python. Saya juga mempelajari indeks, slicing, manipulasi list, perulangan, fungsi, dan perhitungan statistik sederhana.

Materi ini diterapkan dalam praktik analisis nilai mahasiswa untuk menghitung statistik nilai dan menentukan kelulusan berdasarkan batas nilai 60.

## 9. Dokumentasi Git dan GitHub

Program dan hasil latihan didokumentasikan menggunakan Git dan diunggah ke GitHub.
