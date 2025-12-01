import random
import string
alphabet = list(string.ascii_uppercase)


class SubstitutionCipher:
    """
    ShiftCipher class (TO BE COMPLETED).

    Attributes:
        permutation (list): The permutation of the alphabet used as the key. It is a list of uppercase
            characters.
        offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
            a letter's position in the alphabet from 0 (A) to 25 (Z).
    """
    offset = ord('A')

    def __init__(self, permutation: list):
        self.permutation = permutation

    def encrypt(self, plaintext: str):
        """
        TO BE COMPLETED

        Encrypts a plaintext string.
        It should:
            1. Convert lowercase input to uppercase
            2. Leave whitespace and punctuation as is

        Parameters
        ----------
        plaintext : str
            The plaintext string.

        Returns
        -------
        str
            The ciphertext string.
        """
        ciphertext = ''
        return ciphertext

    def decrypt(self, ciphertext: str):
        """
        TO BE COMPLETED

        Decrypts a ciphertext string
        It should:
            1. Convert lowercase input to uppercase
            2. Leave whitespace and punctuation as is

        Parameters
        ----------
        ciphertext : str
            The ciphertext string.

        Returns
        -------
        str
            The plaintext string.
        """
        plaintext = ''
        return plaintext


def main():
    permutation = alphabet.copy()
    random.shuffle(permutation)
    sub_cipher = SubstitutionCipher(permutation)
    ciphertext = sub_cipher.encrypt('The quick brown fox jumps over the lazy dog')
    plaintext = sub_cipher.decrypt(ciphertext)
    assert plaintext == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'


if __name__ == "__main__":
    main()
