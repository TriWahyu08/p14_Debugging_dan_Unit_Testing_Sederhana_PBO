# diskon_service.py
import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        
        # pdb.set_trace() # <-- Diaktifkan untuk debugging
        # pdb.set_trace() # <-- menon-aktifkan debugger agar Unit Test dapat berjalan otomatis hingga selesai.

        # --- BUG LOGIKA DISINI ---
        # Persentase tidak dibagi 100, sehingga diskon 10% dihitung sebagai 1000%
        #jumlah_diskon = harga_awal * persentase_diskon

        # code perbaikan diskon sebelumnya
        # Perbaikan ini membagi persentase dengan 100
        jumlah_diskon = harga_awal * persentase_diskon / 100
        
        harga_setelah_diskon = harga_awal - jumlah_diskon
        
        # --- PERBAIKAN BUG PPN 10% DISINI ---
        # Menghapus BUG: harga_akhir = harga_setelah_diskon * 1.1
        harga_akhir = harga_setelah_diskon 
        # --- PERBAIKAN SELESAI ---

        return harga_akhir

# --- UJI COBA (Ini adalah test case yang akan GAGAL sebelum perbaikan) ---
if __name__ == '__main__':
    calc = DiskonCalculator()
    # Input: 1000 - 10%. Hasil yang diharapkan: 900.0
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil: {hasil}")
    # Output yang benar setelah perbaikan: 900.0
