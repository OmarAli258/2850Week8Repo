import random
import unittest
import exercise1

class TestShiftCipher(unittest.TestCase):
    def test_encryption(self):
        shift_cipher = exercise1.ShiftCipher(13)
        ciphertext = shift_cipher.encrypt("The quick brown fox jumps over the lazy dog")
        self.assertEqual(ciphertext, 'GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT')

    def test_decryption(self):
        shift_cipher = exercise1.ShiftCipher(13)
        plaintext = shift_cipher.decrypt("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT")
        self.assertEqual(plaintext, 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')

    def test_consistency(self):
        shift = random.randint(-25,25)
        shift_cipher = exercise1.ShiftCipher(shift)
        ciphertext = shift_cipher.encrypt("The quick brown fox jumps over the lazy dog")
        plaintext = shift_cipher.decrypt(ciphertext)
        self.assertEqual(plaintext,'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')


if __name__ == '__main__':
    unittest.main()