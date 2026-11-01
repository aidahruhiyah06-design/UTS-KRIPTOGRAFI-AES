
import unittest
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from src.aes_program import main


class TestAESGCM(unittest.TestCase):

    def setUp(self):
        self.key = AESGCM.generate_key(bit_length=128)
        self.nonce = __import__("os").urandom(12)
        self.plaintext = "Aidah Ruhiyah Ramadhani - UTS KRIPTOGRAFI"
        self.aesgcm = AESGCM(self.key)

        self.encrypted_data = self.aesgcm.encrypt(
            self.nonce,
            self.plaintext.encode("utf-8"),
            None
        )

    def test_encryption_and_decryption(self):
        decrypted = self.aesgcm.decrypt(
            self.nonce,
            self.encrypted_data,
            None
        )

        self.assertEqual(
            decrypted.decode("utf-8"),
            self.plaintext
        )

    def test_ciphertext_tampering(self):
        modified = bytearray(self.encrypted_data)
        modified[0] ^= 1

        with self.assertRaises(InvalidTag):
            self.aesgcm.decrypt(
                self.nonce,
                bytes(modified),
                None
            )

    def test_tag_tampering(self):
        modified = bytearray(self.encrypted_data)
        modified[-1] ^= 1

        with self.assertRaises(InvalidTag):
            self.aesgcm.decrypt(
                self.nonce,
                bytes(modified),
                None
            )

    def test_wrong_key(self):
        wrong_key = AESGCM.generate_key(bit_length=128)
        wrong_aesgcm = AESGCM(wrong_key)

        with self.assertRaises(InvalidTag):
            wrong_aesgcm.decrypt(
                self.nonce,
                self.encrypted_data,
                None
            )

    def test_wrong_nonce(self):
        wrong_nonce = bytearray(self.nonce)
        wrong_nonce[0] ^= 1

        with self.assertRaises(InvalidTag):
            self.aesgcm.decrypt(
                bytes(wrong_nonce),
                self.encrypted_data,
                None
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)

