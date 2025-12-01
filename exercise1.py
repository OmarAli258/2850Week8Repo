
class ShiftCipher:
    """
    ShiftCipher class (TO BE COMPLETED).

    Attributes:
        shift (int): The number or letters to shift forward or backward
        offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
            a letter's position in the alphabet from 0 (A) to 25 (Z).
    """

    offset = ord('A')

    def __init__(self, shift: int):
        self.shift = shift

    def __shift_letter(self, letter: str, forward: bool):
        """
        TO BE COMPLETED

        Private method to shift a letter a number of positions forward or backward in the alphabet.

        Parameters
        ----------
        letter : str
            The letter to be shifted.
        forward : bool
            Whether to shift forward (True) or backward (False).

        Returns
        -------
        str
            The shifted letter.
        """
        shifted_letter = ''
        return shifted_letter

    def encrypt(self, plaintext: str):
        """
        TO BE COMPLETED

        Encrypts a plaintext string.
        It should:
            1. Convert lowercase input to uppercase
            2. Leave whitespace and punctuation as is
            3. Use self.__shift_letter to encrypt an individual letter

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
            3. Use self.__shift_letter to decrypt an individual letter

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
    shift_cipher = ShiftCipher(3)
    assert shift_cipher.encrypt('A') == 'D'
    assert shift_cipher.decrypt('B') == 'Y'
    ciphertext = shift_cipher.encrypt('The quick brown fox jumps over the lazy dog')
    plaintext = shift_cipher.decrypt(ciphertext)
    assert plaintext == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'

if __name__ == "__main__":
    main()
