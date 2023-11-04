import unittest

# Fungsi sederhana yang akan diuji
def kali(angka1, angka2):
   hasil = angka1 * angka2
   return hasil

# Kelas untuk unit test
class TestKali(unittest.TestCase):

   # Metode untuk menguji perkalian bilangan positif
   def test_kali_bilangan_positif(self):
       hasil = kali(2, 3)
       self.assertEqual(hasil, 6)

   # Metode untuk menguji perkalian bilangan negatif
   def test_kali_bilangan_negatif(self):
       hasil = kali(-2, 3)
       self.assertEqual(hasil, -6)

   # Metode untuk menguji perkalian bilangan nol
   def test_kali_bilangan_nol(self):
       hasil = kali(5, 0)
       self.assertEqual(hasil, 0)

# Menjalankan unit test
if __name__ == '__main__':
   unittest.main()