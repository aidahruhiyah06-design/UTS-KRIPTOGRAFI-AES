
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def main():
    plaintext = "Aidah Ruhiyah Ramadhani - UTS KRIPTOGRAFI"

    key = AESGCM.generate_key(bit_length=128)
    nonce = os.urandom(12)

    aesgcm = AESGCM(key)

    plaintext_bytes = plaintext.encode("utf-8")

    encrypted_data = aesgcm.encrypt(
        nonce,
        plaintext_bytes,
        None
    )

    ciphertext = encrypted_data[:-16]
    tag = encrypted_data[-16:]

    decrypted_bytes = aesgcm.decrypt(
        nonce,
        encrypted_data,
        None
    )

    decrypted_text = decrypted_bytes.decode("utf-8")

    print("=" * 50)
    print("       PRAKTIKUM AES-128-GCM")
    print("=" * 50)

    print("\nPLAINTEXT")
    print("Teks:", plaintext)
    print("Representasi HEX:", plaintext_bytes.hex().upper())

    print("\nINFORMASI KUNCI")
    print("Algoritma: AES-128-GCM")
    print("Panjang kunci:", len(key) * 8, "bit")
    print("Panjang nonce:", len(nonce) * 8, "bit")
    print("Panjang tag:", len(tag) * 8, "bit")

    print("\nHASIL ENKRIPSI")
    print("Nonce:", nonce.hex().upper())
    print("Ciphertext:", ciphertext.hex().upper())
    print("Authentication Tag:", tag.hex().upper())

    print("\nHASIL DEKRIPSI")
    print("Plaintext:", decrypted_text)

    print("\nVERIFIKASI")
    if decrypted_text == plaintext:
        print("Status: BERHASIL")
        print("Hasil dekripsi sama dengan plaintext awal.")
    else:
        print("Status: GAGAL")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()