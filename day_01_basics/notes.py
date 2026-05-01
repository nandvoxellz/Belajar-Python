# ================================
# DAY 1 - BASICS
# ================================

# --- VARIABLES ---
# variabel adalah wadah untuk menampung nilai
nama = "Nand"
umur = 25
tinggi = 175.5
suka_nasgor = True

# variabel bisa diubah nilainya
umur = 20  # sekarang umur berubah menjadi 20

# penamaan variabel sebaiknya menggunakan huruf kecil dan underscore untuk memisahkan kata
nama_lengkap = "Nand Pratama"

# berikut contoh variabel yang tidak mengikuti konvensi penamaan
NamaLengkap = "Nand Velvette"  # tidak disarankan

#penamaan variabel juga tidak boleh menggunakan spasi atau karakter khusus
# nama lengkap = "Nand Pratama"  # ini salah karena ada spasi
# nama@lengkap = "Nand Pratama"  # ini salah karena ada karakter @

# --- CONSTANTS ---
# konstanta ditulis HURUF_BESAR sebagai konvensi
MAX_SIZE = 100

# Python tidak memiliki konstanta sejati, tetapi kita bisa menggunakan
# konvensi untuk menunjukkan bahwa suatu variabel seharusnya tidak diubah
# MAX_SIZE = 200  # ini sebaiknya dihindari karena MAX_SIZE adalah konstanta

# --- F-STRINGS ---
# f-string adalah cara mudah untuk menggabungkan variabel ke dalam string
nama = "Nand"
umur = 20
pesan = f"Nama saya {nama} dan umur saya {umur} tahun."
# ini berguna untuk membuat string yang lebih mudah dibaca dan ditulis

# --- COMMENTS ---
# komentar digunakan untuk menjelaskan kode, diabaikan oleh Python
# gunakan seperlunya — kode yang baik seharusnya sudah self-explanatory

# komentar juga bisa dipakai untuk "mematikan" kode sementara
# print("ini tidak akan dijalankan")