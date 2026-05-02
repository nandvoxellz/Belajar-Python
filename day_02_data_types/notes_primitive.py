# --- Integers (int) ---
# Integer adalah tipe data yang digunakan untuk menyimpan bilangan bulat, baik positif maupun negatif.
# Contoh penggunaan integer:
umur: int = 20
tahun_lahir: int = 2000

# --- Floating-point numbers (float) ---
# Float adalah tipe data yang digunakan untuk menyimpan bilangan desimal.
tinggi: float = 175.5
berat: float = 68.5

# --- Strings (str) ---
# String adalah tipe data yang digunakan untuk menyimpan teks.
nama: str = "Nand Velvette"
alamat: str = "JL. Industri RT 9 RW 3"

# string juga bisa menggunakan tanda kutip tunggal atau ganda
hobi: str = 'Programmer'
makanan_favorit: str = "nasi goreng"

# jika kamu perlu tanda kutip di dalam string, kamu bisa menggunakan tanda kutip yang berbeda
# atau menggunakan escape character (\)
quote: str = "She said, \"Hello!\""

# string juga bisa digabung (concatenation) menggunakan operator +
greeting: str = "Hello, " + nama
print(greeting) # Output: Hello, Nand Velvette

# string juga bisa diulang (repetition) menggunakan operator *
echo: str = "Echo! " * 3
print(echo) # Output: Echo! Echo! Echo!

# finally, striong juga bisa multi-line menggunakan triple quotes (''' atau """)
multi_line_string: str = """Ini adalah string
yang terdiri dari beberapa baris."""
print(multi_line_string)

# --- Booleans (bool) ---
# Boolean adalah tipe data yang hanya memiliki dua nilai: True atau False.
is_student: bool = True
is_graduate: bool = False

# --- None (NoneType) ---
# None adalah tipe data khusus yang merepresentasikan ketiadaan nilai atau objek.
# None sering digunakan untuk menunjukkan bahwa sebuah variabel belum memiliki nilai
# atau untuk menandai bahwa sebuah fungsi tidak mengembalikan nilai apa pun.

# contoh penggunaan None
def fungsi_tanpa_return() -> None:
    print("Fungsi ini tidak mengembalikan nilai apa pun.")

pilihan_user: str | None = None # variabel ini belum memiliki nilai, jadi kita set ke None
