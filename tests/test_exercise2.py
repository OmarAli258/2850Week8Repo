import random
import string
import unittest
import exercise2

class TestSubstitutionCipher(unittest.TestCase):
    def test_encryption(self):
        permutation = ['Z', 'K', 'T', 'M', 'Y', 'L', 'E', 'A', 'G', 'F', 'H', 'O', 'B', 'N', 'D', 'Q', 'J', 'V', 'X', 'I', 'C', 'W', 'S', 'P', 'R', 'U']
        sub_cipher = exercise2.SubstitutionCipher(permutation)
        ciphertext = sub_cipher.encrypt("The quick brown fox jumps over the lazy dog")
        self.assertEqual(ciphertext, 'IAY JCGTH KVDSN LDP FCBQX DWYV IAY OZUR MDE')

    def test_decryption(self):
        permutation = ['Z', 'K', 'T', 'M', 'Y', 'L', 'E', 'A', 'G', 'F', 'H', 'O', 'B', 'N', 'D', 'Q', 'J', 'V', 'X', 'I', 'C', 'W', 'S', 'P', 'R', 'U']
        sub_cipher = exercise2.SubstitutionCipher(permutation)
        plaintext = sub_cipher.decrypt('IAY JCGTH KVDSN LDP FCBQX DWYV IAY OZUR MDE')
        self.assertEqual(plaintext, 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')

    def test_consistency(self):
        permutation = list(string.ascii_uppercase)
        random.shuffle(permutation)
        sub_cipher = exercise2.SubstitutionCipher(permutation)
        ciphertext = sub_cipher.encrypt("The quick brown fox jumps over the lazy dog")
        plaintext = sub_cipher.decrypt(ciphertext)
        self.assertEqual(plaintext,'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')


if __name__ == '__main__':
    unittest.main()
