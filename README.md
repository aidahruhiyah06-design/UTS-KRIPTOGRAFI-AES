# IMPLEMENTASI ALGORITMA AES-128-GCM MENGGUNAKAN PYTHON

## 1. Deskripsi Proyek

Proyek ini membahas penerapan algoritma Advanced Encryption Standard (AES) dengan mode operasi Galois/Counter Mode (GCM) menggunakan bahasa pemrograman Python. Implementasi dilakukan dengan menggunakan panjang kunci 128 bit untuk melakukan proses enkripsi dan dekripsi terhadap data teks.

Program dirancang untuk memperlihatkan tahapan penggunaan AES-128-GCM, mulai dari pembentukan kunci, pembuatan nonce, proses enkripsi, hingga proses dekripsi. Selain itu, dilakukan pengujian untuk memastikan bahwa data dapat dikembalikan ke bentuk semula dan perubahan pada data terenkripsi dapat terdeteksi.

## 2. Spesifikasi Implementasi

Implementasi program menggunakan spesifikasi sebagai berikut:

| Komponen | Keterangan |
|---|---|
| Algoritma | Advanced Encryption Standard (AES) |
| Mode Operasi | Galois/Counter Mode (GCM) |
| Panjang Kunci | 128 bit |
| Panjang Blok | 128 bit |
| Panjang Nonce | 96 bit |
| Panjang Authentication Tag | 128 bit |
| Bahasa Pemrograman | Python |
| Library | cryptography |
| Pengujian | unittest |

## 3. Fitur Program

Program ini memiliki beberapa fungsi utama, yaitu:

1. Melakukan enkripsi terhadap plaintext menggunakan algoritma AES-128-GCM.
2. Menghasilkan nonce secara acak untuk digunakan dalam proses enkripsi.
3. Menampilkan hasil enkripsi berupa ciphertext dan authentication tag.
4. Melakukan dekripsi untuk mengembalikan ciphertext menjadi plaintext.
5. Membandingkan hasil dekripsi dengan plaintext awal sebagai bentuk verifikasi.
6. Melakukan pengujian terhadap beberapa kondisi, termasuk perubahan ciphertext, perubahan authentication tag, penggunaan kunci yang salah, dan penggunaan nonce yang salah.

## 4. Struktur Direktori Proyek

Proyek ini disusun ke dalam beberapa direktori dan file untuk memisahkan program utama, pengujian, serta dokumentasi hasil pelaksanaan.

```text
KRIPTOGRAFI/
│
├── bukti-pengujian/
│   ├── hasil-enkripsi.png
│   └── hasil-pengujian.png
│
├── src/
│   └── aes_program.py
│
├── tests/
│   └── test_aes.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

Keterangan:
- `src/` berisi kode program utama untuk proses enkripsi dan dekripsi.
- `tests/` berisi kode pengujian program.
- `bukti-pengujian/` menyimpan tangkapan layar hasil pelaksanaan program dan pengujian.
- `requirements.txt` mencantumkan library yang diperlukan.
- `.gitignore` digunakan untuk menentukan file atau direktori yang tidak perlu disertakan dalam pengelolaan Git.
- `README.md` berisi dokumentasi mengenai proyek.

## 5. Instalasi dan Persiapan

Sebelum menjalankan program, pastikan Python telah terpasang pada komputer. Selanjutnya, instal library yang digunakan melalui terminal dengan perintah berikut:

```bash
py -m pip install -r requirements.txt
```

Perintah tersebut digunakan untuk memasang library yang dibutuhkan oleh program berdasarkan daftar dependensi pada file `requirements.txt`.

## 6. Menjalankan Program

Program utama dapat dijalankan melalui terminal menggunakan perintah:

```bash
py src/aes_program.py
```

Setelah program dijalankan, sistem akan menampilkan plaintext, representasi hexadecimal, informasi kunci, nonce, ciphertext, authentication tag, serta hasil dekripsi. Program juga menampilkan status verifikasi untuk menunjukkan kesesuaian antara plaintext awal dan hasil dekripsi.

## 7. Pengujian Program

Pengujian dilakukan menggunakan modul `unittest` yang tersedia pada Python. Pengujian bertujuan untuk mengetahui apakah fungsi enkripsi dan dekripsi berjalan sesuai dengan yang diharapkan serta memastikan bahwa data yang mengalami perubahan tidak dapat diterima sebagai data yang valid.

Untuk menjalankan seluruh pengujian, gunakan perintah:

```bash
py -m unittest discover -s tests -v
```

Skenario pengujian yang diterapkan meliputi:

| No. | Skenario | Tujuan Pengujian |
|---|---|---|
| 1 | Enkripsi dan Dekripsi | Memastikan hasil dekripsi sama dengan plaintext awal. |
| 2 | Perubahan Ciphertext | Memastikan perubahan pada ciphertext dapat terdeteksi. |
| 3 | Perubahan Authentication Tag | Memastikan perubahan pada authentication tag menyebabkan proses dekripsi ditolak. |
| 4 | Penggunaan Kunci yang Salah | Memastikan proses dekripsi gagal apabila menggunakan kunci yang tidak sesuai. |
| 5 | Penggunaan Nonce yang Salah | Memastikan proses dekripsi gagal apabila menggunakan nonce yang berbeda. |

Berdasarkan hasil pelaksanaan pengujian, kelima skenario memperoleh status berhasil (`OK`).

## 8. Aspek Keamanan

Mode GCM pada algoritma AES digunakan untuk memberikan kerahasiaan dan autentikasi data. Authentication tag berperan dalam memeriksa integritas data sehingga perubahan pada ciphertext maupun tag dapat menyebabkan proses dekripsi gagal.

Penggunaan nonce perlu diperhatikan karena nonce tidak boleh digunakan kembali dengan kunci yang sama. Selain itu, kunci enkripsi harus disimpan dengan baik agar tidak diketahui oleh pihak yang tidak berwenang.

Implementasi ini digunakan sebagai bagian dari praktikum mata kuliah Kriptografi untuk mempelajari penerapan algoritma AES-128-GCM menggunakan library kriptografi.

## 9. Dokumentasi Hasil

Dokumentasi pelaksanaan program dan hasil pengujian disimpan dalam direktori `bukti-pengujian`. Dokumentasi tersebut digunakan sebagai bukti bahwa program telah dijalankan dan skenario pengujian telah dilaksanakan.