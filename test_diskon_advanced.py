# test_diskon_advanced.py
import unittest
from diskon_service import DiskonCalculator

class TestDiskonCalculator(unittest.TestCase):
    # Semua Tes dari 1 hingga 4 (Tidak perlu diubah)
    def setUp(self):
        """Arrange: Siapkan instance calculator."""
        self.calc = DiskonCalculator()

    def test_diskon_standar_10_persen(self):
        """Tes 1: Memastikan diskon 10% pada 1000 menghasilkan 900."""
        hasil = self.calc.hitung_diskon(1000, 10)
        self.assertEqual(hasil, 900.0)

    def test_diskon_nol(self):
        """Tes 2 (Boundary): Memastikan diskon 0% tidak mengubah harga."""
        hasil = self.calc.hitung_diskon(500, 0)
        self.assertEqual(hasil, 500.0)

    def test_diskon_batas_atas(self):
        """Tes 3 (Boundary): Memastikan diskon 100% menghasilkan 0."""
        hasil = self.calc.hitung_diskon(750, 100)
        self.assertEqual(hasil, 0.0)

    def test_input_negatif(self):
        """Tes 4 (Boundary): Memastikan input diskon negatif dilarang dan menghasilkan harga awal."""
        hasil = self.calc.hitung_diskon(500, -5)
        self.assertGreaterEqual(hasil, 500) 


class TestDiskonLanjut(unittest.TestCase):
    # Class baru untuk tes lanjutan (Langkah D.3.a)
    
    def setUp(self):
        """Arrange: Siapkan instance calculator."""
        self.calc = DiskonCalculator()

    def test_uji_nilai_float(self):
        """Tes 5: Uji nilai float (diskon 33% pada 999). Menggunakan assertAlmostEqual."""
        # Harga seharusnya: 999 - (999 * 0.33) = 999 - 329.67 = 669.33
        # ACT
        hasil = self.calc.hitung_diskon(999.0, 33)
        # ASSERT
        self.assertAlmostEqual(hasil, 669.33, places=2) # places=2 untuk akurasi 2 desimal

    def test_uji_edge_case_harga_nol(self):
        """Tes 6: Uji Edge Case (harga awal 0). Hasil harus 0."""
        # ACT
        hasil = self.calc.hitung_diskon(0, 10)
        # ASSERT
        self.assertEqual(hasil, 0.0)

if __name__ == '__main__':
    unittest.main()
    