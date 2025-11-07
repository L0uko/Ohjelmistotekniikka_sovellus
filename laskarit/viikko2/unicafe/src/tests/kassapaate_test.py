import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
        self.maksukortti=Maksukortti(100)
    def test_saldo(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_saldo_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)

    def test_ei_myytyja_edullisia(self):
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_ei_myytyja_maukkaita(self):
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_edullinen_kateisella(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihto,260)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_edullinen_ei_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)

    def test_maukas_kateisella(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihto,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_maukas_ei_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200),200)


#    def test_maukas_kateisella(self):
#        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200),200)
        
    def test_edullinen_kortilla(self):
        self.maksukortti.lataa_rahaa(240)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_maukas_kortilla(self):
        self.maksukortti.lataa_rahaa(400)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_edullinene_kortilla_ei_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),False)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)
        
    def test_maukas_kortilla_ei_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),False)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_laita_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100200)

    def test_laita_rahaa_kortille_ei_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)