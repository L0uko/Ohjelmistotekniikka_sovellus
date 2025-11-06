import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo,1000)

    def test_rahan_lisays(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo,1100)

    def test_rahan_ottaminen(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo,500)
    
    def test_rahan_ottaminen_liian_vahan(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo,1000)

    def test_onnistunut_maksu_palauttaa_true(self):
        
        self.assertEqual(self.maksukortti.ota_rahaa(500),True)

    def test_epäonnistunut_maksu_palauttaa_false(self):
        
        self.assertEqual(self.maksukortti.ota_rahaa(2000),False)