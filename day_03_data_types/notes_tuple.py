# --- Tuple (tuple) ---
# Tuple adalah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel. 
# Tuple dibuat dengan menggunakan tanda kurung biasa () dan item-item di dalamnya dipisahkan dengan koma.

# properti tuple:

# Dapat diubah? (mutable): Tidak
# Dapat menyimpan tipe data campuran (heterogen): Ya
# Dapat menyimpan duplikat: Ya
# Dapat diindeks: Ya

# Contoh penggunaan tuple
koordinat: tuple[int, int] = (10, 20)
nama: tuple[str, str] = ("Nand", "Miwa")
elemen_campuran: tuple[str, int, bool] = ("Nand", 20, True)
tuple_duplikat: tuple[int, ...] = (1, 2, 4, 4, 4, 6, 7)
# bisa menggunakan ... untuk menunjukkan bahwa tipe data yang sama dapat muncul berulang kali dalam tuple

# cara membuat tuple kosong

# constructor tuple
tuple_kosong: tuple = ()

# tuple dengan satu item harus diikuti dengan koma
tuple_satu_item: tuple[int] = (42,)
# jika tidak, Python akan menganggapnya sebagai tipe data biasa (dalam hal ini, int) dan bukan tuple

# beberapa operasi dasar pada tuple

# len: menghitung jumlah item dalam tuple
jumlah_item: int = len(koordinat) # output: 2

# index: mencari indeks pertama dari item tertentu dalam tuple
indeks_20: int = koordinat.index(20) # output: 1

# count: menghitung jumlah kemunculan item tertentu dalam tuple
jumlah_4: int = tuple_duplikat.count(4) # output: 3

# concatenation tuple
tuple1: tuple[int, int] = (1, 2)
tuple2: tuple[int, int] = (3, 4)
hasil: tuple[int, ...] = tuple1 + tuple2  # output: (1, 2, 3, 4)