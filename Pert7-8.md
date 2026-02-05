# PERTEMUAN 7-8: QUEUE BERBASIS ARRAY

## SUMMARY MATERI

### 1. Pengertian Queue

**Queue** (Antrian) adalah struktur data linear yang mengikuti prinsip **FIFO (First In First Out)**, yang berarti elemen yang pertama masuk akan menjadi yang pertama keluar.

**Analogi:**
- Seperti antrian di kasir: orang yang datang pertama akan dilayani pertama
- Seperti antrian printer: dokumen yang dikirim pertama akan dicetak pertama
- Seperti antrian tiket: yang mengambil nomor pertama akan dipanggil pertama

**Karakteristik Queue:**
- Penambahan elemen dilakukan di **REAR** (belakang)
- Penghapusan elemen dilakukan di **FRONT** (depan)
- Mengikuti prinsip FIFO (First In First Out)
- Bersifat linear dan dinamis
- Memiliki dua pointer: FRONT dan REAR

### 2. Operasi Dasar Queue

Queue memiliki beberapa operasi fundamental:

| Operasi | Deskripsi | Keterangan |
|---------|-----------|------------|
| `enqueue(el)` | Menambahkan elemen ke belakang queue | Memasukkan elemen di REAR |
| `dequeue()` | Menghapus dan mengembalikan elemen depan | Mengeluarkan elemen dari FRONT |
| `front()` / `peek()` | Melihat elemen depan tanpa menghapus | Membaca nilai FRONT tanpa mengubah queue |
| `isEmpty()` | Mengecek apakah queue kosong | Return True jika kosong |
| `clear()` | Mengosongkan seluruh queue | Menghapus semua elemen |
| `size()` | Mengembalikan jumlah elemen | Menghitung total elemen dalam queue |

### 3. Implementasi Queue dengan Array

Queue dapat diimplementasikan menggunakan **array** dengan dua pendekatan:

#### A. Simple Queue (Linear Queue)
**Masalah:** Terjadi "false overflow" - array penuh padahal masih ada ruang kosong di depan

#### B. Circular Queue (Recommended)
**Solusi:** Menggunakan konsep circular array dimana REAR bisa kembali ke awal

**Variabel yang Dibutuhkan:**
- `pool[]` : Array untuk menyimpan elemen-elemen queue
- `front` : Index elemen pertama
- `rear` : Index elemen terakhir
- `size` : Jumlah elemen dalam queue

**Konsep Circular Queue:**
```
Rumus:
- front = (front + 1) % MAX_SIZE
- rear = (rear + 1) % MAX_SIZE
```

**Ilustrasi Circular Queue:**
```
    [0] [1] [2] [3] [4]
     ↓               ↓
   FRONT          REAR

Setelah beberapa enqueue/dequeue:
    [5] [ ] [ ] [1] [2]
          ↑       ↓
        REAR   FRONT
```

### 4. Implementasi Queue di Python

Python menggunakan **List** atau **collections.deque** untuk implementasi queue:

```python
class Queue:
    def __init__(self):
        self.pool = []

    def enqueue(self, element):
        """Menambahkan elemen ke belakang queue"""
        self.pool.append(element)

    def dequeue(self):
        """Menghapus dan mengembalikan elemen depan"""
        if self.isEmpty():
            return None
        return self.pool.pop(0)

    def front(self):
        """Melihat elemen depan tanpa menghapus"""
        if self.isEmpty():
            return None
        return self.pool[0]

    def isEmpty(self):
        """Mengecek apakah queue kosong"""
        return len(self.pool) == 0

    def clear(self):
        """Mengosongkan queue"""
        self.pool.clear()

    def size(self):
        """Mengembalikan jumlah elemen"""
        return len(self.pool)
```

**Alternatif dengan collections.deque (Lebih Efisien):**
```python
from collections import deque

class Queue:
    def __init__(self):
        self.pool = deque()

    def enqueue(self, element):
        self.pool.append(element)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.pool.popleft()  # O(1) - lebih cepat dari pop(0)
```

### 5. Kompleksitas Waktu Queue

| Operasi | List | deque |
|---------|------|-------|
| `enqueue()` | O(1) | O(1) |
| `dequeue()` | **O(n)** | **O(1)** ⭐ |
| `front()` | O(1) | O(1) |
| `isEmpty()` | O(1) | O(1) |
| `size()` | O(1) | O(1) |

**Rekomendasi:** Gunakan `collections.deque` untuk performa lebih baik pada operasi `dequeue()`.

### 6. Aplikasi Queue dalam Pemrograman

Queue digunakan dalam berbagai aplikasi:

1. **CPU Scheduling**: Antrian proses untuk dieksekusi
2. **Print Spooling**: Antrian dokumen untuk dicetak
3. **BFS (Breadth-First Search)**: Traversal graph/tree level by level
4. **Buffer**: Streaming data, keyboard buffer
5. **Call Center**: Sistem antrian panggilan telepon
6. **Task Scheduling**: Antrian tugas untuk diproses
7. **Network Packet**: Antrian paket data dalam router
8. **Message Queue**: Sistem komunikasi antar aplikasi

### 7. Queue vs Stack

| Aspek | Queue | Stack |
|-------|-------|-------|
| Prinsip | FIFO (First In First Out) | LIFO (Last In First Out) |
| Operasi Insert | enqueue() di REAR | push() di TOP |
| Operasi Remove | dequeue() di FRONT | pop() di TOP |
| Pointer | 2 (FRONT, REAR) | 1 (TOP) |
| Use Case | Scheduling, BFS | Undo, Recursion, DFS |

### 8. Jenis-jenis Queue

1. **Simple Queue**: Queue standar dengan FIFO
2. **Circular Queue**: Queue dengan konsep circular array
3. **Priority Queue**: Elemen dengan prioritas tertinggi keluar pertama
4. **Deque (Double-ended Queue)**: Insert dan delete di kedua ujung
5. **Input-restricted Deque**: Insert hanya di satu ujung
6. **Output-restricted Deque**: Delete hanya di satu ujung

---

## DEMO PYTHON

### Demo 1: Implementasi Dasar Queue

```python
"""
Demo 1: Implementasi Dasar Queue
Demonstrasi class Queue dengan operasi-operasi dasar
"""

class Queue:
    def __init__(self):
        self.pool = []

    def enqueue(self, element):
        """Menambahkan elemen ke belakang queue"""
        self.pool.append(element)
        print(f"  Enqueue: {element}")

    def dequeue(self):
        """Menghapus dan mengembalikan elemen depan"""
        if self.isEmpty():
            print("  Queue kosong! Tidak dapat dequeue.")
            return None
        element = self.pool.pop(0)
        print(f"  Dequeue: {element}")
        return element

    def front(self):
        """Melihat elemen depan tanpa menghapus"""
        if self.isEmpty():
            return None
        return self.pool[0]

    def rear(self):
        """Melihat elemen belakang"""
        if self.isEmpty():
            return None
        return self.pool[-1]

    def isEmpty(self):
        """Mengecek apakah queue kosong"""
        return len(self.pool) == 0

    def clear(self):
        """Mengosongkan queue"""
        self.pool.clear()
        print("  Queue cleared!")

    def size(self):
        """Mengembalikan jumlah elemen"""
        return len(self.pool)

    def display(self):
        """Menampilkan isi queue"""
        if self.isEmpty():
            print("  Queue: []")
        else:
            print(f"  Queue: {self.pool} (FRONT: {self.front()}, REAR: {self.rear()})")


print("=" * 60)
print("DEMO 1: IMPLEMENTASI DASAR QUEUE")
print("=" * 60)

# Membuat queue baru
queue = Queue()
print("\n1. Queue baru (kosong):")
queue.display()
print(f"   isEmpty: {queue.isEmpty()}")
print(f"   Size: {queue.size()}")

# Enqueue beberapa elemen
print("\n2. Enqueue elemen 10, 20, 30:")
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

# Melihat front dan rear
print(f"\n3. Front: {queue.front()}, Rear: {queue.rear()}")
queue.display()

# Dequeue elemen
print("\n4. Dequeue 2 elemen:")
queue.dequeue()
queue.dequeue()
queue.display()

# Enqueue lagi
print("\n5. Enqueue elemen 40, 50:")
queue.enqueue(40)
queue.enqueue(50)
queue.display()
print(f"   Size: {queue.size()}")

# Clear queue
print("\n6. Clear queue:")
queue.clear()
queue.display()

# Dequeue dari queue kosong
print("\n7. Coba dequeue dari queue kosong:")
queue.dequeue()
```

**Output:**
```
============================================================
DEMO 1: IMPLEMENTASI DASAR QUEUE
============================================================

1. Queue baru (kosong):
  Queue: []
   isEmpty: True
   Size: 0

2. Enqueue elemen 10, 20, 30:
  Enqueue: 10
  Enqueue: 20
  Enqueue: 30
  Queue: [10, 20, 30] (FRONT: 10, REAR: 30)

3. Front: 10, Rear: 30
  Queue: [10, 20, 30] (FRONT: 10, REAR: 30)

4. Dequeue 2 elemen:
  Dequeue: 10
  Dequeue: 20
  Queue: [30] (FRONT: 30, REAR: 30)

5. Enqueue elemen 40, 50:
  Enqueue: 40
  Enqueue: 50
  Queue: [30, 40, 50] (FRONT: 30, REAR: 50)
   Size: 3

6. Clear queue:
  Queue cleared!
  Queue: []

7. Coba dequeue dari queue kosong:
  Queue kosong! Tidak dapat dequeue.
```

---

### Demo 2: Queue dengan collections.deque

```python
"""
Demo 2: Queue menggunakan collections.deque
Implementasi yang lebih efisien untuk operasi dequeue
"""

from collections import deque

class EfficientQueue:
    def __init__(self):
        self.pool = deque()

    def enqueue(self, element):
        """Menambahkan elemen ke belakang queue"""
        self.pool.append(element)
        print(f"  Enqueue: {element}")

    def dequeue(self):
        """Menghapus dan mengembalikan elemen depan"""
        if self.isEmpty():
            print("  Queue kosong! Tidak dapat dequeue.")
            return None
        element = self.pool.popleft()  # O(1) - lebih cepat!
        print(f"  Dequeue: {element}")
        return element

    def front(self):
        """Melihat elemen depan tanpa menghapus"""
        if self.isEmpty():
            return None
        return self.pool[0]

    def isEmpty(self):
        """Mengecek apakah queue kosong"""
        return len(self.pool) == 0

    def size(self):
        """Mengembalikan jumlah elemen"""
        return len(self.pool)

    def display(self):
        """Menampilkan isi queue"""
        if self.isEmpty():
            print("  Queue: []")
        else:
            print(f"  Queue: {list(self.pool)} (FRONT: {self.front()})")


print("=" * 60)
print("DEMO 2: QUEUE DENGAN COLLECTIONS.DEQUE")
print("=" * 60)

queue = EfficientQueue()

print("\n1. Enqueue 5 elemen:")
for i in range(1, 6):
    queue.enqueue(i * 10)

queue.display()

print("\n2. Dequeue 3 elemen:")
for _ in range(3):
    queue.dequeue()

queue.display()

print("\n3. Enqueue 3 elemen lagi:")
for i in range(6, 9):
    queue.enqueue(i * 10)

queue.display()

print("\n4. Performance comparison:")
print("   List-based queue: dequeue() is O(n)")
print("   Deque-based queue: dequeue() is O(1) ✓")
```

**Output:**
```
============================================================
DEMO 2: QUEUE DENGAN COLLECTIONS.DEQUE
============================================================

1. Enqueue 5 elemen:
  Enqueue: 10
  Enqueue: 20
  Enqueue: 30
  Enqueue: 40
  Enqueue: 50
  Queue: [10, 20, 30, 40, 50] (FRONT: 10)

2. Dequeue 3 elemen:
  Dequeue: 10
  Dequeue: 20
  Dequeue: 30
  Queue: [40, 50] (FRONT: 40)

3. Enqueue 3 elemen lagi:
  Enqueue: 60
  Enqueue: 70
  Enqueue: 80
  Queue: [40, 50, 60, 70, 80] (FRONT: 40)

4. Performance comparison:
   List-based queue: dequeue() is O(n)
   Deque-based queue: dequeue() is O(1) ✓
```

---

### Demo 3: Aplikasi - Sistem Antrian Bank

```python
"""
Demo 3: Aplikasi Queue - Sistem Antrian Bank
Simulasi sistem antrian nasabah di bank
"""

from collections import deque
import time

class Customer:
    """Class untuk merepresentasikan nasabah"""
    def __init__(self, number, name, service_type):
        self.number = number
        self.name = name
        self.service_type = service_type

    def __str__(self):
        return f"#{self.number} - {self.name} ({self.service_type})"


class BankQueue:
    """Sistem antrian bank"""
    def __init__(self):
        self.queue = deque()
        self.counter = 0
        self.served_count = 0

    def take_number(self, name, service_type):
        """Nasabah mengambil nomor antrian"""
        self.counter += 1
        customer = Customer(self.counter, name, service_type)
        self.queue.append(customer)
        print(f"\n✓ Nomor antrian: {self.counter}")
        print(f"  Nama: {name}")
        print(f"  Layanan: {service_type}")
        print(f"  Jumlah antrian: {len(self.queue)} orang")

    def call_next(self):
        """Memanggil nasabah berikutnya"""
        if len(self.queue) == 0:
            print("\n⚠ Tidak ada antrian")
            return None

        customer = self.queue.popleft()
        self.served_count += 1

        print(f"\n🔔 Memanggil: {customer}")
        print(f"  Sisa antrian: {len(self.queue)} orang")
        return customer

    def show_queue(self):
        """Menampilkan daftar antrian"""
        print("\n" + "=" * 60)
        print("DAFTAR ANTRIAN SAAT INI")
        print("=" * 60)

        if len(self.queue) == 0:
            print("Tidak ada antrian")
        else:
            for i, customer in enumerate(self.queue, 1):
                print(f"{i}. {customer}")

        print(f"\nTotal antrian: {len(self.queue)} orang")
        print(f"Total sudah dilayani: {self.served_count} orang")


print("=" * 60)
print("DEMO 3: SISTEM ANTRIAN BANK")
print("=" * 60)

bank = BankQueue()

# Simulasi nasabah mengambil nomor
print("\n--- NASABAH MENGAMBIL NOMOR ---")
bank.take_number("Budi Santoso", "Setor Tunai")
bank.take_number("Ani Wijaya", "Tarik Tunai")
bank.take_number("Citra Dewi", "Transfer")
bank.take_number("Doni Pratama", "Pembukaan Rekening")
bank.take_number("Eka Putri", "Setor Tunai")

# Tampilkan antrian
bank.show_queue()

# Panggil beberapa nasabah
print("\n\n--- PEMANGGILAN NASABAH ---")
bank.call_next()
bank.call_next()

# Tampilkan antrian setelah pemanggilan
bank.show_queue()

# Nasabah baru datang
print("\n\n--- NASABAH BARU DATANG ---")
bank.take_number("Fajar Nugroho", "Pembayaran")

# Panggil lagi
print("\n\n--- PEMANGGILAN NASABAH ---")
bank.call_next()
bank.call_next()

# Tampilkan antrian akhir
bank.show_queue()
```

**Output:**
```
============================================================
DEMO 3: SISTEM ANTRIAN BANK
============================================================

--- NASABAH MENGAMBIL NOMOR ---

✓ Nomor antrian: 1
  Nama: Budi Santoso
  Layanan: Setor Tunai
  Jumlah antrian: 1 orang

✓ Nomor antrian: 2
  Nama: Ani Wijaya
  Layanan: Tarik Tunai
  Jumlah antrian: 2 orang

✓ Nomor antrian: 3
  Nama: Citra Dewi
  Layanan: Transfer
  Jumlah antrian: 3 orang

✓ Nomor antrian: 4
  Nama: Doni Pratama
  Layanan: Pembukaan Rekening
  Jumlah antrian: 4 orang

✓ Nomor antrian: 5
  Nama: Eka Putri
  Layanan: Setor Tunai
  Jumlah antrian: 5 orang

============================================================
DAFTAR ANTRIAN SAAT INI
============================================================
1. #1 - Budi Santoso (Setor Tunai)
2. #2 - Ani Wijaya (Tarik Tunai)
3. #3 - Citra Dewi (Transfer)
4. #4 - Doni Pratama (Pembukaan Rekening)
5. #5 - Eka Putri (Setor Tunai)

Total antrian: 5 orang
Total sudah dilayani: 0 orang


--- PEMANGGILAN NASABAH ---

🔔 Memanggil: #1 - Budi Santoso (Setor Tunai)
  Sisa antrian: 4 orang

🔔 Memanggil: #2 - Ani Wijaya (Tarik Tunai)
  Sisa antrian: 3 orang

============================================================
DAFTAR ANTRIAN SAAT INI
============================================================
1. #3 - Citra Dewi (Transfer)
2. #4 - Doni Pratama (Pembukaan Rekening)
3. #5 - Eka Putri (Setor Tunai)

Total antrian: 3 orang
Total sudah dilayani: 2 orang


--- NASABAH BARU DATANG ---

✓ Nomor antrian: 6
  Nama: Fajar Nugroho
  Layanan: Pembayaran
  Jumlah antrian: 4 orang


--- PEMANGGILAN NASABAH ---

🔔 Memanggil: #3 - Citra Dewi (Transfer)
  Sisa antrian: 3 orang

🔔 Memanggil: #4 - Doni Pratama (Pembukaan Rekening)
  Sisa antrian: 2 orang

============================================================
DAFTAR ANTRIAN SAAT INI
============================================================
1. #5 - Eka Putri (Setor Tunai)
2. #6 - Fajar Nugroho (Pembayaran)

Total antrian: 2 orang
Total sudah dilayani: 4 orang
```

---

### Demo 4: Aplikasi - Print Job Scheduler

```python
"""
Demo 4: Aplikasi Queue - Print Job Scheduler
Simulasi antrian dokumen untuk dicetak
"""

from collections import deque

class PrintJob:
    """Class untuk merepresentasikan job print"""
    def __init__(self, job_id, document_name, pages, user):
        self.job_id = job_id
        self.document_name = document_name
        self.pages = pages
        self.user = user

    def __str__(self):
        return f"Job#{self.job_id}: {self.document_name} ({self.pages} pages) - {self.user}"


class PrinterQueue:
    """Sistem antrian printer"""
    def __init__(self, printer_name):
        self.printer_name = printer_name
        self.queue = deque()
        self.job_counter = 0
        self.total_printed = 0

    def add_job(self, document_name, pages, user):
        """Menambahkan job print ke antrian"""
        self.job_counter += 1
        job = PrintJob(self.job_counter, document_name, pages, user)
        self.queue.append(job)

        print(f"\n✓ Job ditambahkan: {job}")
        print(f"  Posisi antrian: {len(self.queue)}")

    def print_next(self):
        """Mencetak job berikutnya"""
        if len(self.queue) == 0:
            print("\n⚠ Tidak ada job dalam antrian")
            return None

        job = self.queue.popleft()
        self.total_printed += job.pages

        print(f"\n🖨️  Printing: {job}")
        print(f"  Status: Printing {job.pages} pages...")
        print(f"  Sisa antrian: {len(self.queue)} jobs")

        return job

    def show_queue(self):
        """Menampilkan daftar antrian print"""
        print("\n" + "=" * 70)
        print(f"PRINTER: {self.printer_name}")
        print("=" * 70)

        if len(self.queue) == 0:
            print("Status: Idle (tidak ada antrian)")
        else:
            print(f"Status: {len(self.queue)} jobs in queue")
            print("\nAntrian:")
            total_pages = 0
            for i, job in enumerate(self.queue, 1):
                print(f"  {i}. {job}")
                total_pages += job.pages

            print(f"\nTotal halaman dalam antrian: {total_pages} pages")

        print(f"Total sudah dicetak: {self.total_printed} pages")
        print("=" * 70)

    def cancel_all(self):
        """Membatalkan semua job"""
        count = len(self.queue)
        self.queue.clear()
        print(f"\n⚠️  {count} jobs dibatalkan")


print("=" * 70)
print("DEMO 4: PRINT JOB SCHEDULER")
print("=" * 70)

printer = PrinterQueue("Canon LBP-6030")

# Menambahkan beberapa print jobs
print("\n--- MENAMBAHKAN PRINT JOBS ---")
printer.add_job("Laporan_Keuangan.pdf", 25, "Budi")
printer.add_job("Proposal_Proyek.docx", 15, "Ani")
printer.add_job("Presentasi.pptx", 10, "Citra")
printer.add_job("Data_Mahasiswa.xlsx", 5, "Doni")

# Tampilkan antrian
printer.show_queue()

# Print beberapa job
print("\n\n--- PROCESSING PRINT JOBS ---")
printer.print_next()
printer.print_next()

# Tampilkan antrian setelah print
printer.show_queue()

# Tambah job baru
print("\n\n--- MENAMBAH JOB BARU ---")
printer.add_job("Invoice.pdf", 3, "Eka")

# Print sisa job
print("\n\n--- PROCESSING REMAINING JOBS ---")
printer.print_next()
printer.print_next()

# Tampilkan status akhir
printer.show_queue()

# Tambah job lagi dan cancel
print("\n\n--- TEST CANCEL ---")
printer.add_job("Test1.pdf", 10, "User1")
printer.add_job("Test2.pdf", 20, "User2")
printer.show_queue()
printer.cancel_all()
printer.show_queue()
```

**Output:**
```
======================================================================
DEMO 4: PRINT JOB SCHEDULER
======================================================================

--- MENAMBAHKAN PRINT JOBS ---

✓ Job ditambahkan: Job#1: Laporan_Keuangan.pdf (25 pages) - Budi
  Posisi antrian: 1

✓ Job ditambahkan: Job#2: Proposal_Proyek.docx (15 pages) - Ani
  Posisi antrian: 2

✓ Job ditambahkan: Job#3: Presentasi.pptx (10 pages) - Citra
  Posisi antrian: 3

✓ Job ditambahkan: Job#4: Data_Mahasiswa.xlsx (5 pages) - Doni
  Posisi antrian: 4

======================================================================
PRINTER: Canon LBP-6030
======================================================================
Status: 4 jobs in queue

Antrian:
  1. Job#1: Laporan_Keuangan.pdf (25 pages) - Budi
  2. Job#2: Proposal_Proyek.docx (15 pages) - Ani
  3. Job#3: Presentasi.pptx (10 pages) - Citra
  4. Job#4: Data_Mahasiswa.xlsx (5 pages) - Doni

Total halaman dalam antrian: 55 pages
Total sudah dicetak: 0 pages
======================================================================


--- PROCESSING PRINT JOBS ---

🖨️  Printing: Job#1: Laporan_Keuangan.pdf (25 pages) - Budi
  Status: Printing 25 pages...
  Sisa antrian: 3 jobs

🖨️  Printing: Job#2: Proposal_Proyek.docx (15 pages) - Ani
  Status: Printing 15 pages...
  Sisa antrian: 2 jobs

======================================================================
PRINTER: Canon LBP-6030
======================================================================
Status: 2 jobs in queue

Antrian:
  1. Job#3: Presentasi.pptx (10 pages) - Citra
  2. Job#4: Data_Mahasiswa.xlsx (5 pages) - Doni

Total halaman dalam antrian: 15 pages
Total sudah dicetak: 40 pages
======================================================================


--- MENAMBAH JOB BARU ---

✓ Job ditambahkan: Job#5: Invoice.pdf (3 pages) - Eka
  Posisi antrian: 3


--- PROCESSING REMAINING JOBS ---

🖨️  Printing: Job#3: Presentasi.pptx (10 pages) - Citra
  Status: Printing 10 pages...
  Sisa antrian: 2 jobs

🖨️  Printing: Job#4: Data_Mahasiswa.xlsx (5 pages) - Doni
  Status: Printing 5 pages...
  Sisa antrian: 1 jobs

======================================================================
PRINTER: Canon LBP-6030
======================================================================
Status: 1 jobs in queue

Antrian:
  1. Job#5: Invoice.pdf (3 pages) - Eka

Total halaman dalam antrian: 3 pages
Total sudah dicetak: 55 pages
======================================================================


--- TEST CANCEL ---

✓ Job ditambahkan: Job#6: Test1.pdf (10 pages) - User1
  Posisi antrian: 2

✓ Job ditambahkan: Job#7: Test2.pdf (20 pages) - User2
  Posisi antrian: 3

======================================================================
PRINTER: Canon LBP-6030
======================================================================
Status: 3 jobs in queue

Antrian:
  1. Job#5: Invoice.pdf (3 pages) - Eka
  2. Job#6: Test1.pdf (10 pages) - User1
  3. Job#7: Test2.pdf (20 pages) - User2

Total halaman dalam antrian: 33 pages
Total sudah dicetak: 55 pages
======================================================================

⚠️  3 jobs dibatalkan

======================================================================
PRINTER: Canon LBP-6030
======================================================================
Status: Idle (tidak ada antrian)
Total sudah dicetak: 55 pages
======================================================================
```

---

## CARA MENJALANKAN DEMO

Semua file demo dapat dijalankan langsung menggunakan Python.

### Persiapan Awal

1. **Pastikan Python sudah terinstall**
   ```bash
   python --version
   ```

2. **Navigasi ke folder pert7-8**
   ```bash
   cd d:\_CodeDev\strukturdatadanalgoritma\pert7-8
   ```

### Menjalankan Demo

1. **Demo 1 - Implementasi Dasar Queue**
   ```bash
   python demo1_queue_basic.py
   ```
   Yang akan ditampilkan:
   - Operasi enqueue, dequeue, front
   - Display isi queue
   - Size dan isEmpty
   - Clear queue

2. **Demo 2 - Queue dengan deque**
   ```bash
   python demo2_efficient_queue.py
   ```
   Yang akan ditampilkan:
   - Implementasi dengan collections.deque
   - Perbandingan performa dengan list
   - Operasi enqueue/dequeue

3. **Demo 3 - Sistem Antrian Bank**
   ```bash
   python demo3_bank_queue.py
   ```
   Yang akan ditampilkan:
   - Simulasi sistem antrian bank
   - Pengambilan nomor antrian
   - Pemanggilan nasabah
   - Statistik antrian

4. **Demo 4 - Print Job Scheduler**
   ```bash
   python demo4_print_scheduler.py
   ```
   Yang akan ditampilkan:
   - Simulasi antrian printer
   - Penambahan dan pemrosesan job
   - Pembatalan job
   - Status printer

---

## LATIHAN SOAL

### Soal 1: Sistem Antrian Restoran

**Deskripsi:**
Buatlah sistem antrian untuk restoran cepat saji menggunakan Queue.

**Spesifikasi:**

1. Buatlah class `Order` dengan atribut:
   - `order_id` (int): Nomor pesanan
   - `customer_name` (string): Nama pelanggan
   - `items` (list): Daftar menu yang dipesan
   - `total_price` (int): Total harga

2. Buatlah class `RestaurantQueue` dengan fungsi:
   - `add_order(customer_name, items, total_price)`: Menambahkan pesanan
   - `serve_next()`: Melayani pesanan berikutnya
   - `show_queue()`: Menampilkan antrian pesanan
   - `total_revenue()`: Menghitung total pendapatan dari pesanan yang sudah dilayani

**Contoh Output yang Diharapkan:**
```
=== SISTEM ANTRIAN RESTORAN ===

1. Tambah Order:
   Order #1: Budi - [Burger, Fries] - Rp 45000
   Posisi antrian: 1

2. Tambah Order:
   Order #2: Ani - [Pizza, Coke] - Rp 55000
   Posisi antrian: 2

3. Serve next:
   🍔 Serving: Order #1 - Budi
   Sisa antrian: 1

4. Total revenue: Rp 45000
```

---

### Soal 2: Circular Queue dengan Ukuran Tetap

**Deskripsi:**
Implementasikan **Circular Queue** dengan ukuran tetap (fixed size) menggunakan array.

**Spesifikasi:**

1. Buatlah class `CircularQueue` dengan:
   - `max_size`: Ukuran maksimum queue
   - `front`: Pointer ke elemen depan
   - `rear`: Pointer ke elemen belakang
   - `pool`: Array untuk menyimpan elemen

2. Implementasikan fungsi:
   - `enqueue(element)`: Menambah elemen (check penuh)
   - `dequeue()`: Menghapus elemen (check kosong)
   - `isFull()`: Mengecek apakah queue penuh
   - `isEmpty()`: Mengecek apakah queue kosong
   - `display()`: Menampilkan isi queue dan posisi front/rear

3. Gunakan rumus circular:
   - `rear = (rear + 1) % max_size`
   - `front = (front + 1) % max_size`

**Contoh Output yang Diharapkan:**
```
=== CIRCULAR QUEUE (Max Size: 5) ===

1. Enqueue 10, 20, 30:
   Queue: [10, 20, 30, None, None]
   Front: 0, Rear: 2

2. Dequeue 2 elemen:
   Queue: [None, None, 30, None, None]
   Front: 2, Rear: 2

3. Enqueue 40, 50, 60, 70:
   Queue: [60, 70, 30, 40, 50]
   Front: 2, Rear: 1 (wrapped around!)

4. Coba enqueue 80:
   Error: Queue is full!
```

**Hint:** Gunakan `(rear + 1) % max_size == front` untuk cek queue penuh.

---

## TIPS PENGERJAAN

1. **Pahami prinsip FIFO**: Elemen pertama masuk akan keluar pertama
2. **Gunakan collections.deque**: Lebih efisien untuk operasi dequeue
3. **Circular queue**: Gunakan modulo (%) untuk wrapping index
4. **Selalu cek isEmpty()**: Sebelum dequeue atau front
5. **Debug dengan display**: Tampilkan isi queue dan pointer di setiap langkah
6. **Test edge cases**: Queue kosong, queue penuh (circular), single element

**Selamat mengerjakan! 🚀**

---

*Catatan: File ini merupakan bagian dari materi Struktur Data dan Algoritma - Pertemuan 7-8*
