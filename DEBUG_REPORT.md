# **DEBUG REPORT - Praktikum 14: Bug PPN 10%**

**Waktu Debugging:** [12/12/2025]
**File yang Diuji:** diskon_service.py

### 1. Deskripsi Kegagalan (Failing Test)

Ketika menjalankan tes standar (Harga Awal: 1000, Diskon: 10%, Hasil Seharusnya: 900.0), program menghasilkan: **990.0** (Karena 900 + 10% PPN = 990). Program tidak mengembalikan 900.0 seperti yang diharapkan, menunjukkan adanya biaya tambahan.

### 2. Langkah Penelusuran (Menggunakan pdb)

Tujuan: Menemukan dari mana nilai 990.0 berasal.

1.  **Aktivasi pdb:** Menghapus komentar pada `pdb.set_trace()` di awal `hitung_diskon`.
2.  **Eksekusi:** Menjalankan `python diskon_service.py`. Program berhenti.

| Perintah `pdb` | Penjelasan | Variabel yang Dicetak (`p [variabel]`) | Nilai yang Ditemukan | Bukti PPN Dihitung |
| :--- | :--- | :--- | :--- | :--- |
| `n` | Melangkah ke perhitungan `jumlah_diskon`. | `p jumlah_diskon` | `100.0` | Diskon benar. |
| `n` | Melangkah ke perhitungan `harga_setelah_diskon`. | `p harga_setelah_diskon` | `900.0` | Harga setelah diskon benar. |
| `n` | Melangkah ke baris `harga_akhir = harga_setelah_diskon * 1.1`. **(BUG LINE)** | `p harga_akhir` | *Belum ada nilai* | |
| `n` | Melaksanakan baris PPN. | `p harga_akhir` | `990.0` | **BUG TERKONFIRMASI.** Nilai 900.0 dikalikan 1.1. |
| `c` | Melanjutkan eksekusi. | `p hasil` (di luar fungsi) | `990.0` | Hasil akhir 990.0. |

### 3. Akar Masalah (Root Cause)

* Variabel `harga_setelah_diskon` bernilai `900.0` (Nilai yang benar).
* Pada baris `harga_akhir = harga_setelah_diskon * 1.1`, harga dinaikkan 10% (**900.0 * 1.1 = 990.0**), menyalahi logika fungsi yang hanya seharusnya menghitung diskon.

### 4. Perbaikan

Menghapus baris `harga_akhir = harga_setelah_diskon * 1.1` dan mengganti `harga_akhir` dengan `harga_setelah_diskon`.

**Kode yang Dihapus (BUG):**
```python
harga_akhir = harga_setelah_diskon * 1.1