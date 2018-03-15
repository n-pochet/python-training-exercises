import unittest

from caesar_cipher import encrypt

class CaesarCipherTest(unittest.TestCase):

    def test_encrypt_none(self):
        self.assertEqual(encrypt(None), "")
    
    def test_encrypt_empty(self):
        self.assertEqual(encrypt(""), "")
    
    def test_encrypt_ABC(self):
        self.assertEqual(encrypt("ABC"), "DEF")
    
    def test_encrypt_XYZ(self):
        self.assertEqual(encrypt("XYZ"), "ABC")
    
    def test_encrypt_xyz(self):
        self.assertEqual(encrypt("xyz"), "abc")

    def test_encrypt_abc(self):
        self.assertEqual(encrypt("abc"), "def")
    
    def test_encrypt_sentence(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        encrypted_sentence = "wkh#txlfn#eurzq#ira#mxpsv#ryhu#wkh#odcb#grj"
        self.assertEqual(encrypt(sentence), encrypted_sentence)

if __name__ == "__main__":
    unittest.main()