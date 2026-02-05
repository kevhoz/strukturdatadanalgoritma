# PERTEMUAN 3-4: ARRAY

## SUMMARY MATERI

### 1. Pengertian Array
**Array** atau **Larik** adalah struktur data yang berisi sejumlah data secara berurutan dengan susunan elemen yang sama. Setiap elemen dalam array dapat diakses menggunakan **indeks** yang menyatakan urutan penempatan data.

**Karakteristik Array:**
- Kumpulan item-item data yang homogen (tipe data sama)
- Dapat dipilih menggunakan indeks saat program dijalankan
- Dapat dibentuk dari tipe data primitif atau struktur/record
- Disimpan secara berurutan dalam memori

### 2. Dimensi Array

**a. Array 1 Dimensi**
- Struktur paling sederhana (array linier)
- Digunakan untuk menyatakan himpunan atau sejumlah record
- Contoh: `[10, 20, 30, 40, 50]`

**b. Array 2 Dimensi**
- Digunakan untuk menyatakan matriks atau tabel
- Memiliki indeks baris dan kolom
- Contoh: Matriks 3x3, tabel koordinat
- Susunan: **Row-Major Order** (per baris) atau **Column-Major Order** (per kolom)

**c. Array 3 Dimensi**
- Digunakan untuk menyatakan sekumpulan matriks/tabel
- Contoh: Data 3D, kubus data

### 3. Deklarasi Array di Python

Python menggunakan **List** sebagai implementasi array dinamis:

```python
# Array kosong
arr = []

# Array dengan nilai awal
arr = [1, 2, 3, 4, 5]

# Array 2D
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 4. Operasi Dasar Array

| Operasi | Syntax Python | Keterangan |
|---------|---------------|------------|
| Menambah elemen di akhir | `arr.append(x)` | Menambah x ke akhir array |
| Menambah di posisi tertentu | `arr.insert(i, x)` | Menyisipkan x di indeks i |
| Menghapus elemen | `arr.pop(i)` | Menghapus elemen di indeks i |
| Menghapus by value | `arr.remove(x)` | Menghapus elemen dengan nilai x |
| Mengakses elemen | `arr[i]` | Akses elemen di indeks i |
| Mengubah elemen | `arr[i] = x` | Ubah nilai di indeks i |
| Panjang array | `len(arr)` | Menghitung jumlah elemen |
| Mengurutkan | `arr.sort()` | Urutkan array ascending |
| Membalik urutan | `arr.reverse()` | Balik urutan array |

### 5. Array Statis vs Array Dinamis

**Array Statis (Bahasa Gen 3: C, Pascal)**
- Ukuran harus dideklarasikan di awal
- Ukuran tidak dapat berubah
- Contoh: `int arr[10];` (C++)

**Array Dinamis (Bahasa Gen 4: Python)**
- Ukuran dapat berubah-ubah
- Tidak perlu deklarasi ukuran
- Lebih fleksibel
- Contoh: `arr = []` (Python)

### 6. Record dengan Array

**Record/Structure** adalah sekumpulan data dengan tipe data yang sama atau berbeda yang "dipaketkan" bersama.

Di Python, record diimplementasikan dengan **Class**:

```python
class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

# Array of Records
data_mhs = []
data_mhs.append(Mahasiswa("Budi", "001", 85))
data_mhs.append(Mahasiswa("Ani", "002", 90))
```

---

## DEMO PYTHON

### Demo 1: Operasi Dasar Array 1 Dimensi

```python
"""
Demo 1: Operasi Dasar Array 1 Dimensi
Demonstrasi penggunaan list/array untuk menyimpan data nilai mahasiswa
"""

# Membuat array nilai mahasiswa
nilai = [85, 90, 78, 92, 88]

print("=" * 50)
print("DEMO 1: OPERASI DASAR ARRAY 1 DIMENSI")
print("=" * 50)

# Menampilkan array
print(f"\nArray nilai awal: {nilai}")
print(f"Jumlah mahasiswa: {len(nilai)}")

# Mengakses elemen
print(f"\nNilai mahasiswa ke-1 (indeks 0): {nilai[0]}")
print(f"Nilai mahasiswa ke-3 (indeks 2): {nilai[2]}")

# Menambah nilai baru
nilai.append(95)
print(f"\nSetelah tambah nilai 95: {nilai}")

# Menambah di posisi tertentu
nilai.insert(2, 87)
print(f"Setelah insert nilai 87 di indeks 2: {nilai}")

# Mengubah nilai
nilai[0] = 86
print(f"Setelah ubah nilai indeks 0 menjadi 86: {nilai}")

# Menghitung statistik
rata_rata = sum(nilai) / len(nilai)
nilai_max = max(nilai)
nilai_min = min(nilai)

print(f"\n--- STATISTIK ---")
print(f"Rata-rata: {rata_rata:.2f}")
print(f"Nilai tertinggi: {nilai_max}")
print(f"Nilai terendah: {nilai_min}")

# Mengurutkan
nilai_sorted = sorted(nilai)  # tidak mengubah array asli
print(f"\nNilai terurut (ascending): {nilai_sorted}")

nilai.sort(reverse=True)  # mengubah array asli
print(f"Nilai terurut (descending): {nilai}")
```

**Output:**
```
==================================================
DEMO 1: OPERASI DASAR ARRAY 1 DIMENSI
==================================================

Array nilai awal: [85, 90, 78, 92, 88]
Jumlah mahasiswa: 5

Nilai mahasiswa ke-1 (indeks 0): 85
Nilai mahasiswa ke-3 (indeks 2): 78

Setelah tambah nilai 95: [85, 90, 78, 92, 88, 95]
Setelah insert nilai 87 di indeks 2: [85, 90, 87, 78, 92, 88, 95]
Setelah ubah nilai indeks 0 menjadi 86: [86, 90, 87, 78, 92, 88, 95]

--- STATISTIK ---
Rata-rata: 88.00
Nilai tertinggi: 95
Nilai terendah: 78

Nilai terurut (ascending): [78, 86, 87, 88, 90, 92, 95]
Nilai terurut (descending): [95, 92, 90, 88, 87, 86, 78]
```

---

### Demo 2: Array 2 Dimensi - Matriks

```python
"""
Demo 2: Array 2 Dimensi - Matriks
Demonstrasi operasi matriks dan akses elemen 2D
"""

print("=" * 50)
print("DEMO 2: ARRAY 2 DIMENSI - MATRIKS")
print("=" * 50)

# Membuat matriks 3x3
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatriks A (3x3):")
for baris in matriks:
    print(baris)

# Mengakses elemen
print(f"\nElemen di baris 0, kolom 0: {matriks[0][0]}")
print(f"Elemen di baris 1, kolom 2: {matriks[1][2]}")
print(f"Elemen di baris 2, kolom 1: {matriks[2][1]}")

# Mengubah elemen
matriks[1][1] = 50
print("\nSetelah mengubah matriks[1][1] menjadi 50:")
for baris in matriks:
    print(baris)

# Operasi pada matriks
print("\n--- OPERASI MATRIKS ---")

# Transpose matriks
transpose = [[matriks[j][i] for j in range(len(matriks))]
             for i in range(len(matriks[0]))]
print("\nTranspose Matriks:")
for baris in transpose:
    print(baris)

# Sum setiap baris
print("\nJumlah setiap baris:")
for i, baris in enumerate(matriks):
    print(f"Baris {i}: {sum(baris)}")

# Sum setiap kolom
print("\nJumlah setiap kolom:")
for j in range(len(matriks[0])):
    total = sum(matriks[i][j] for i in range(len(matriks)))
    print(f"Kolom {j}: {total}")

# Diagonal utama
diagonal = [matriks[i][i] for i in range(len(matriks))]
print(f"\nDiagonal utama: {diagonal}")
print(f"Sum diagonal utama: {sum(diagonal)}")

# Penjumlahan dua matriks
matriks_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("\nMatriks B (3x3):")
for baris in matriks_b:
    print(baris)

hasil_tambah = [[matriks[i][j] + matriks_b[i][j]
                 for j in range(len(matriks[0]))]
                for i in range(len(matriks))]

print("\nMatriks A + B:")
for baris in hasil_tambah:
    print(baris)
```

**Output:**
```
==================================================
DEMO 2: ARRAY 2 DIMENSI - MATRIKS
==================================================

Matriks A (3x3):
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Elemen di baris 0, kolom 0: 1
Elemen di baris 1, kolom 2: 6
Elemen di baris 2, kolom 1: 8

Setelah mengubah matriks[1][1] menjadi 50:
[1, 2, 3]
[4, 50, 6]
[7, 8, 9]

--- OPERASI MATRIKS ---

Transpose Matriks:
[1, 4, 7]
[2, 50, 8]
[3, 6, 9]

Jumlah setiap baris:
Baris 0: 6
Baris 1: 60
Baris 2: 24

Jumlah setiap kolom:
Kolom 0: 12
Kolom 1: 60
Kolom 2: 18

Diagonal utama: [1, 50, 9]
Sum diagonal utama: 60

Matriks B (3x3):
[9, 8, 7]
[6, 5, 4]
[3, 2, 1]

Matriks A + B:
[10, 10, 10]
[10, 55, 10]
[10, 10, 10]
```

---

### Demo 3: Array of Records (Array dari Objek)

```python
"""
Demo 3: Array of Records
Demonstrasi penggunaan array untuk menyimpan data mahasiswa
menggunakan class (record)
"""

print("=" * 50)
print("DEMO 3: ARRAY OF RECORDS (CLASS)")
print("=" * 50)

# Definisi Class Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"{self.nim:10} {self.nama:20} {self.nilai:5}"

    def get_grade(self):
        if self.nilai >= 85:
            return 'A'
        elif self.nilai >= 70:
            return 'B'
        elif self.nilai >= 60:
            return 'C'
        elif self.nilai >= 50:
            return 'D'
        else:
            return 'E'

# Membuat array of records
data_mahasiswa = []
data_mahasiswa.append(Mahasiswa("001", "Budi Santoso", 85))
data_mahasiswa.append(Mahasiswa("002", "Ani Wijaya", 92))
data_mahasiswa.append(Mahasiswa("003", "Citra Dewi", 78))
data_mahasiswa.append(Mahasiswa("004", "Doni Pratama", 88))
data_mahasiswa.append(Mahasiswa("005", "Eka Putri", 95))

# Menampilkan data
print("\nDATA MAHASISWA:")
print("=" * 50)
print(f"{'NIM':10} {'Nama':20} {'Nilai':5} {'Grade':5}")
print("-" * 50)

for mhs in data_mahasiswa:
    print(f"{mhs}  {mhs.get_grade():5}")

# Mencari mahasiswa dengan nilai tertinggi
mhs_terbaik = max(data_mahasiswa, key=lambda m: m.nilai)
print(f"\nMahasiswa dengan nilai tertinggi:")
print(f"  Nama  : {mhs_terbaik.nama}")
print(f"  NIM   : {mhs_terbaik.nim}")
print(f"  Nilai : {mhs_terbaik.nilai}")

# Menghitung rata-rata
total_nilai = sum(mhs.nilai for mhs in data_mahasiswa)
rata_rata = total_nilai / len(data_mahasiswa)
print(f"\nRata-rata nilai kelas: {rata_rata:.2f}")

# Filter mahasiswa dengan grade A
mahasiswa_A = [mhs for mhs in data_mahasiswa if mhs.get_grade() == 'A']
print(f"\nMahasiswa dengan Grade A ({len(mahasiswa_A)} orang):")
for mhs in mahasiswa_A:
    print(f"  - {mhs.nama} (Nilai: {mhs.nilai})")

# Sorting berdasarkan nama
data_mahasiswa.sort(key=lambda m: m.nama)
print("\nData mahasiswa setelah di-sort berdasarkan nama:")
print("-" * 50)
for mhs in data_mahasiswa:
    print(f"{mhs}  {mhs.get_grade():5}")
```

**Output:**
```
==================================================
DEMO 3: ARRAY OF RECORDS (CLASS)
==================================================

DATA MAHASISWA:
==================================================
NIM        Nama                 Nilai Grade
--------------------------------------------------
001        Budi Santoso            85  A
002        Ani Wijaya              92  A
003        Citra Dewi              78  B
004        Doni Pratama            88  A
005        Eka Putri               95  A

Mahasiswa dengan nilai tertinggi:
  Nama  : Eka Putri
  NIM   : 005
  Nilai : 95

Rata-rata nilai kelas: 87.60

Mahasiswa dengan Grade A (4 orang):
  - Budi Santoso (Nilai: 85)
  - Ani Wijaya (Nilai: 92)
  - Doni Pratama (Nilai: 88)
  - Eka Putri (Nilai: 95)

Data mahasiswa setelah di-sort berdasarkan nama:
--------------------------------------------------
002        Ani Wijaya              92  A
001        Budi Santoso            85  A
003        Citra Dewi              78  B
004        Doni Pratama            88  A
005        Eka Putri               95  A
```

---

### Demo 4: Aplikasi Praktis - Tabel Penjualan

```python
"""
Demo 4: Aplikasi Praktis - Tabel Penjualan Bulanan
Demonstrasi penggunaan array 2D untuk data penjualan
"""

print("=" * 70)
print("DEMO 4: TABEL PENJUALAN BULANAN")
print("=" * 70)

# Data penjualan: Baris = Produk, Kolom = Bulan (Jan-Jun)
produk = ["Laptop", "Mouse", "Keyboard", "Monitor"]
bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"]

# Data penjualan (unit)
penjualan = [
    [15, 20, 18, 22, 25, 30],  # Laptop
    [50, 45, 60, 55, 65, 70],  # Mouse
    [35, 40, 38, 42, 45, 50],  # Keyboard
    [10, 12, 15, 14, 18, 20]   # Monitor
]

# Harga per unit (dalam ribu rupiah)
harga = [5000, 50, 150, 1500]

# Menampilkan tabel penjualan
print("\nTABEL PENJUALAN (dalam unit)")
print("=" * 70)
print(f"{'Produk':12}", end="")
for b in bulan:
    print(f"{b:>8}", end="")
print(f"{'Total':>8}")
print("-" * 70)

for i, prod in enumerate(produk):
    print(f"{prod:12}", end="")
    total_unit = 0
    for j in range(len(bulan)):
        print(f"{penjualan[i][j]:8}", end="")
        total_unit += penjualan[i][j]
    print(f"{total_unit:8}")

# Total penjualan per bulan
print("-" * 70)
print(f"{'Total':12}", end="")
for j in range(len(bulan)):
    total_bulan = sum(penjualan[i][j] for i in range(len(produk)))
    print(f"{total_bulan:8}", end="")
grand_total = sum(sum(row) for row in penjualan)
print(f"{grand_total:8}")

# Menghitung pendapatan
print("\n" + "=" * 70)
print("PENDAPATAN (dalam juta rupiah)")
print("=" * 70)
print(f"{'Produk':12}", end="")
for b in bulan:
    print(f"{b:>10}", end="")
print(f"{'Total':>12}")
print("-" * 70)

total_pendapatan_per_produk = []
for i, prod in enumerate(produk):
    print(f"{prod:12}", end="")
    total_pendapatan = 0
    for j in range(len(bulan)):
        pendapatan = penjualan[i][j] * harga[i]
        print(f"{pendapatan/1000:10.1f}", end="")
        total_pendapatan += pendapatan
    total_pendapatan_per_produk.append(total_pendapatan)
    print(f"{total_pendapatan/1000:12.1f}")

# Produk terlaris
print("\n--- ANALISIS ---")
produk_terlaris_idx = 0
max_unit = 0
for i in range(len(produk)):
    total_unit = sum(penjualan[i])
    if total_unit > max_unit:
        max_unit = total_unit
        produk_terlaris_idx = i

print(f"Produk terlaris (unit): {produk[produk_terlaris_idx]} ({max_unit} unit)")

# Produk dengan pendapatan tertinggi
produk_pendapatan_idx = total_pendapatan_per_produk.index(max(total_pendapatan_per_produk))
print(f"Produk pendapatan tertinggi: {produk[produk_pendapatan_idx]} "
      f"(Rp {total_pendapatan_per_produk[produk_pendapatan_idx]/1000:.1f} juta)")

# Bulan dengan penjualan tertinggi
total_per_bulan = [sum(penjualan[i][j] for i in range(len(produk)))
                   for j in range(len(bulan))]
bulan_terbaik_idx = total_per_bulan.index(max(total_per_bulan))
print(f"Bulan dengan penjualan tertinggi: {bulan[bulan_terbaik_idx]} "
      f"({total_per_bulan[bulan_terbaik_idx]} unit)")
```

**Output:**
```
======================================================================
DEMO 4: TABEL PENJUALAN BULANAN
======================================================================

TABEL PENJUALAN (dalam unit)
======================================================================
Produk          Jan     Feb     Mar     Apr     Mei     Jun   Total
----------------------------------------------------------------------
Laptop           15      20      18      22      25      30     130
Mouse            50      45      60      55      65      70     345
Keyboard         35      40      38      42      45      50     250
Monitor          10      12      15      14      18      20      89
----------------------------------------------------------------------
Total           110     117     131     133     153     170     814

======================================================================
PENDAPATAN (dalam juta rupiah)
======================================================================
Produk          Jan       Feb       Mar       Apr       Mei       Jun       Total
----------------------------------------------------------------------
Laptop         75.0     100.0      90.0     110.0     125.0     150.0       650.0
Mouse           2.5       2.2       3.0       2.8       3.2       3.5        17.2
Keyboard        5.2       6.0       5.7       6.3       6.8       7.5        37.5
Monitor        15.0      18.0      22.5      21.0      27.0      30.0       133.5

--- ANALISIS ---
Produk terlaris (unit): Mouse (345 unit)
Produk pendapatan tertinggi: Laptop (Rp 650.0 juta)
Bulan dengan penjualan tertinggi: Jun (170 unit)
```

---

## LATIHAN SOAL

### Soal 1: Pengelolaan Data Buku Perpustakaan

**Deskripsi:**
Buatlah program sederhana untuk mengelola data buku di perpustakaan menggunakan **array of records (class)**.

**Spesifikasi:**

1. Buatlah **class Buku** dengan atribut:
   - `kode_buku` (string)
   - `judul` (string)
   - `pengarang` (string)
   - `stok` (integer)

2. Buatlah **array/list** untuk menyimpan minimal 5 data buku

3. Program harus memiliki fungsi-fungsi berikut:
   - `tampilkan_semua_buku()`: Menampilkan seluruh data buku dalam bentuk tabel
   - `cari_buku(kode)`: Mencari dan menampilkan buku berdasarkan kode buku
   - `buku_habis()`: Menampilkan daftar buku yang stoknya 0 (habis dipinjam)
   - `total_buku()`: Menghitung total seluruh buku yang tersedia

**Contoh Output yang Diharapkan:**
```
=== DATA BUKU PERPUSTAKAAN ===

Kode    Judul                    Pengarang           Stok
------------------------------------------------------------
B001    Python untuk Pemula      John Doe            5
B002    Algoritma Dasar          Jane Smith          3
B003    Struktur Data            Ahmad Zaki          0
B004    Pemrograman Web          Siti Nurhaliza      7
B005    Basis Data               Budi Santoso        2

Total buku tersedia: 17 buku

BUKU YANG HABIS DIPINJAM:
- B003: Struktur Data (Pengarang: Ahmad Zaki)
```

### Soal 2: Nilai Ujian Mahasiswa

**Deskripsi:**
Buatlah program untuk mengolah nilai ujian mahasiswa menggunakan **array 2 dimensi**.

**Spesifikasi:**

1. Buatlah program yang menyimpan nilai ujian untuk:
   - **4 mahasiswa** (baris)
   - **3 mata kuliah** (kolom): Matematika, Pemrograman, Basis Data

2. Data nilai dapat berupa array 2D, contoh:
   ```python
   # Baris = Mahasiswa, Kolom = Mata Kuliah
   nilai = [
       [85, 90, 88],  # Mahasiswa 1
       [75, 80, 82],  # Mahasiswa 2
       [90, 95, 92],  # Mahasiswa 3
       [70, 75, 78]   # Mahasiswa 4
   ]
   ```

3. Program harus dapat menghitung dan menampilkan:
   - **Tabel nilai** mahasiswa
   - **Rata-rata nilai per mahasiswa**
   - **Rata-rata nilai per mata kuliah**
   - **Mahasiswa dengan rata-rata tertinggi**
   - **Jumlah mahasiswa yang lulus** (rata-rata >= 75)

**Contoh Output yang Diharapkan:**
```
=== NILAI UJIAN MAHASISWA ===

Mahasiswa    Matematika  Pemrograman  Basis Data  Rata-rata
-------------------------------------------------------------
Mahasiswa 1      85          90           88        87.67
Mahasiswa 2      75          80           82        79.00
Mahasiswa 3      90          95           92        92.33
Mahasiswa 4      70          75           78        74.33

-------------------------------------------------------------
Rata-rata MK:    80.00       85.00        85.00

=== HASIL ANALISIS ===
Mahasiswa terbaik: Mahasiswa 3 (Rata-rata: 92.33)
Jumlah mahasiswa lulus (>= 75): 3 orang
```

## TIPS PENGERJAAN

1. **Mulai dengan perencanaan**: Buat pseudocode atau flowchart sebelum coding
2. **Test secara bertahap**: Uji setiap fungsi sebelum lanjut ke fungsi berikutnya
3. **Gunakan fungsi**: Pisahkan logic ke dalam fungsi-fungsi kecil
4. **Format output dengan rapi**: Gunakan f-string dan formatting untuk tampilan yang baik
5. **Tambahkan validasi**: Cek input user dan handle error yang mungkin terjadi

**Selamat mengerjakan! 🚀**

---

*Catatan: File ini merupakan bagian dari materi Struktur Data dan Algoritma - Pertemuan 3-4*
