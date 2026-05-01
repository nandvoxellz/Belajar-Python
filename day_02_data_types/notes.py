# ================================
# DAY 2 - DATA TYPES
# ================================

# --- TYPE HINTS ---
# Type hints adalah cara untuk memberikan informasi tentang
# tipe data yang digunakan dalam kode kita. Ini membantu
# kita dan orang lain yang membaca kode kita untuk memahami
# apa jenis data yang diharapkan dan digunakan dalam fungsi atau variabel.
#   penggunaan type hints:
nama: str = "Stelle"
umur: int = 3
tinggi: float = 175.5
my_istri: bool = True

# apalah wajib? Tidak,
# tapi sangat membantu untuk meningkatkan keterbacaan kode dan mengurangi kesalahan tipe data.
# name = "Stelle"  # tanpa type hint juga bisa, tapi kita tidak tahu tipe data apa yang diharapkan.

# --- TYPE CONVERSION ---
# Type conversion adalah proses mengubah satu tipe data menjadi tipe data lain.
# Contoh type conversion:

# Mengubah string ke integer
angka_str: str = "123"
angka_int: int = int(angka_str)  # type conversion dari string ke integer
# perlu diketahu bahwa alphabet tidak bisa diubah ke integer

# Mengubah integer ke string
angka_int: int = 456
angka_str: str = str(angka_int)  # type conversion dari integer ke string
